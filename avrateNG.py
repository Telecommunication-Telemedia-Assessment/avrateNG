#!/usr/bin/env python3
"""
    avrateNG main script

    This file is part of avrateNG.
    avrateNG is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    avrateNG is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with avrateNG.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
import argparse
import json
import threading
import webbrowser
import time
import datetime
import random
from platform import system

# load libs from lib directory
import loader
from log import *
from system import *

import bottle
from bottle import Bottle
from bottle import auth_basic
from bottle import route
from bottle import run
from bottle import install
from bottle import template
from bottle import request
from bottle import redirect
from bottle import response
from bottle import error
from bottle import static_file
from bottle_sqlite import SQLitePlugin
from bottle_config import ConfigPlugin

from post_rating import *


def check_credentials(username, password):
    config = ConfigPlugin._config
    validName = config["http_user_name"]
    validPassword = config["http_user_password"]
    return password == validPassword and username == validName


def play(config, video_index, playlist):
    if config.get("no_video_playback", False):
        return
    def q(x):
        return "\"" + x + "\""
    video = " ".join(map(q, config[playlist][video_index]))

    lInfo("play {}".format(video))

    if "gray_video" in config:
        video = q(config["gray_video"]) + " " + video + " " + q(config["gray_video"])
        lInfo("use gray video before and after: {}".format(video))
    lInfo("player command")
    print(config["player"].format(filename=video))
    shell_call(config["player"].format(filename=video))


@route('/')  # Welcome screen
@auth_basic(check_credentials)
def welcome(db, config):

    # for every new start ("/"): user_id (cookie) is incremented by 1
    if not db.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='ratings'").fetchone():
        user_id = 1 # if ratings table does not exist: first user_id = 1
    else:
        user_id = int(db.execute('SELECT max(user_ID) from ratings').fetchone()[0]) + 1  # new user_ID is always old (highest) user_ID+1
    response.set_cookie("user_id", str(user_id), path="/")

    # initialize session_state variable (throws error when refreshing the page or going back)
    response.set_cookie("session_state", "0", path="/")

    # generate new shuffled playlist for every participant when shuffle mode is active
    if config["shuffle"]:
        config["shuffled_playlist"] = random.sample(config["playlist"],len(config["playlist"]))

    # check if training stage is wished and/or training has already finished:
    if config["trainingsplaylist"]: # check if training switch is toggled
        if not request.get_cookie("training_state") == "done": # Cookie that controls if training was already done or is still open
            response.set_cookie("training_state","open", path="/")
            response.set_cookie("training", "1", path="/")
            return template(config["template_folder"] + "/training_welcome.tpl", title="AvRateNG", user_id=user_id)
        else:
            response.set_cookie("training", "0", path="/")
            return template(config["template_folder"] + "/welcome.tpl", title="AvRateNG", user_id=user_id)
    else:
        response.set_cookie("training","0", path="/")
        return template(config["template_folder"] + "/welcome.tpl", title="AvRateNG", user_id=user_id)


@route('/rate/<video_index>')  # Rating screen with video_index as variable
@auth_basic(check_credentials)
def rate(db, config, video_index):

    video_index = int(video_index)
    user_id = int(request.get_cookie("user_id"))
    session_state = int(request.get_cookie("session_state"))

    # Select correct playlist for lookup
    if int(request.get_cookie("training")):
        playlist = "trainingsplaylist"
    else:
        if config["shuffle"]:
            playlist = "shuffled_playlist"
        else:
            playlist = "playlist"

    # Check if video should be played or was already watched
    if video_index == session_state:
        play_video = 1
    else:
        play_video = 0

    # play video only on first visit
    if play_video == 1:
        play(config, video_index, playlist)
        # play just one time
        play_video = 0
        session_state = session_state + 1
        response.set_cookie("session_state", str(session_state), path="/")

    return template(config["template_folder"] + "/rate1.tpl", title="AvRateNG", rating_template=config["rating_template"], video_index=video_index, video_count=len(config[playlist]), user_id=user_id, question=config.get("question", "add question to config.json"))


@route('/about')  # About section
@auth_basic(check_credentials)
def about(config):
    return template(config["template_folder"] + "/about.tpl", title="AvRateNG")


@route('/info')  # User Info screen
@auth_basic(check_credentials)
def info(config):
    if not config.get("demographics_form", True):
        return redirect('/rate/0')
    return template(config["template_folder"] + "/demographicInfo.tpl", title="AvRateNG")


@route('/finish')  # Finish screen
@auth_basic(check_credentials)
def finish(config):
    return template(config["template_folder"] + "/finish.tpl", title="AvRateNG")


@route('/statistics')
@auth_basic(check_credentials)
def statistics(db, config):
    # Get Data and video names for ratings and transform to JSON objects (better handling)
    db_data=db.execute("SELECT video_name,rating,rating_type from ratings").fetchall()
    video_names = [row[0] for row in db_data]
    rating_data = [int(row[1]) for row in db_data]
    rating_types = [row[2] for row in db_data]
    # extract all kinds of ratings from DB and convert to one dictionary
    rating_dict = {}
    for idx, video in enumerate(video_names):
        rating_dict.setdefault(rating_types[idx], {}).setdefault(video, []).append(rating_data[idx])

    # return dictionary as JSON as interface to Java script (see statistics.tpl file for further info)
    return template(config["template_folder"] + "/statistics.tpl", title="AvRateNG", rating_dict=json.dumps(rating_dict))


def store_rating_key_value_pair(db, config, user_id, timestamp, video_index, key, value, tracker, training=False):
    def get_video_name(playlist, video_index, config):
        video_name = config[playlist][int(video_index)]
        # for supporting multiple files per playlist entry, here needs to be done some extension
        if len(video_name) == 0:
            # old style of storing, one video name per rating
            video_name = video_name[0]
        else:
            # complex video name, e.g. two videos
            video_name = str(video_name)
        return video_name

    # Choose DB table to store the ratings
    if not training:

        # Lookup the correct playlist
        if config["shuffle"]:
            playlist = "shuffled_playlist"
        else:
            playlist = "playlist"
        video_name = get_video_name(playlist, video_index, config)

        # Store rating to DB
        db.execute('CREATE TABLE IF NOT EXISTS ratings (user_ID INTEGER, video_ID TEXT, video_name TEXT, rating_type TEXT, rating TEXT, timestamp TEXT);')
        db.execute('INSERT INTO ratings VALUES (?,?,?,?,?,?);',(user_id, video_index, video_name, key, value, timestamp))
        db.commit()

        # Store mouse tracking data to DB
        db.execute('CREATE TABLE IF NOT EXISTS tracker (user_ID INTEGER, video_ID TEXT, video_name TEXT, tracker TEXT);')
        db.execute('INSERT INTO tracker VALUES (?,?,?,?);',(user_id, video_index, video_name, tracker))
        db.commit()

    else:
        playlist = "trainingsplaylist"
        video_name = get_video_name(playlist, video_index, config)
        db.execute('CREATE TABLE IF NOT EXISTS training (user_ID INTEGER, video_ID TEXT, video_name TEXT, rating_type TEXT, rating TEXT, timestamp TEXT);')
        db.execute('INSERT INTO training VALUES (?,?,?,?,?,?);',(user_id, video_index, video_name, key, value, timestamp))
        db.commit()

    return playlist


@route('/save_rating', method='POST')
@auth_basic(check_credentials)
def saveRating(db, config):  # save rating for watched video
    video_index = request.query.video_index  # extract current video_index from query
    timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S %f'))  # define timestamp
    user_id = int(request.get_cookie("user_id"))

    # Get Mousetracker and write to DB
    if "mouse_track" in request.forms:
        tracker = request.forms["mouse_track"]
        del request.forms["mouse_track"]
    else:
        tracker = "No tracking data submitted."

    # Get POST Data ratings and write to DB
    if len(request.forms.keys()) >= 1:
        request_data_pairs = {}
        for item in request.forms:
            request_data_pairs[item] = request.forms.get(item)
    else:
        lError("The submitted rating form does not contain any key/value pairs.")

    training = int(request.get_cookie("training"))
    for key, value in request_data_pairs.items():
        playlist = store_rating_key_value_pair(db, config, user_id, timestamp, video_index, key, value, tracker, training)

    lInfo("selected playlist: {}".format(playlist))
    # check if this was the last video in playlist
    video_index = int(video_index) + 1
    if video_index > len(config[playlist]) - 1:  # playlist over
        if training == 1:
            lInfo("training done")
            response.set_cookie("training_state", "done", path="/")
            redirect('/')
        else:
            lInfo("training not over")
            response.set_cookie("training_state", "open", path="/")

            if config['display_feedback_form']:
                redirect('/feedback')
            else:
                redirect('/finish')
    else:
        redirect('/rate/' + str(video_index))  # next video


@route('/save_demographics', method='POST')
@auth_basic(check_credentials)
def saveDemographics(db, config):  # save user information (user_id is key in tables) as JSON string
    user_id = int(request.get_cookie("user_id"))

    db.execute('CREATE TABLE IF NOT EXISTS info (user_ID, info_json TEXT);')
    db.execute('INSERT INTO info VALUES (?,?);',(user_id, json.dumps(dict(request.forms))))
    db.commit()

    redirect('/rate/0')


@route('/static/<filename:path>',name='static')  # access the stylesheets and static files (JS files,...)
@auth_basic(check_credentials)
def server_static(filename,config):
    # needed for routing the static files (CSS)
    this_dir_path = os.path.dirname(os.path.abspath(__file__))
    return static_file(filename, root=this_dir_path + '/'+ config["template_folder"]  +'/static')


def server(config, host="127.0.0.1"):
    install(SQLitePlugin(dbfile='ratings.db'))
    install(ConfigPlugin(config))

    lInfo("server starting.")
    run(
        host=host,
        port=config["http_port"],
        debug=True,
        reloader=True,
        fast=True
    )
    lInfo("server stopped.")


@route('/reset_cookies')
@auth_basic(check_credentials)
def reset_cookies(db, config):
    for cookie in request.cookies:
        response.set_cookie(cookie, '', expires=0)


def get_and_check_playlist(playlistfilename):
    with open(playlistfilename) as playlistfile:
        playlist = []
        for line in playlistfile:
            if line.strip() == "":
                continue
            normalized_video_path = os.path.join(*line.strip().split("/"))
            # check if each video exists
            if " | " in normalized_video_path:
                lInfo("specified multiple videos per playlist entry")
            videos = normalized_video_path.split(" | ")
            for video in videos:
                if not os.path.isfile(video):
                    lError("'{}' is not a valid videofile, please check your playlistfile".format(normalized_video_path))
                    sys.exit(-1)
            playlist.append(videos)
        print("\n".join(map(str, playlist)))
        return playlist
    return -1


def main(params=[]):
    parser = argparse.ArgumentParser(description='avrateNG', epilog="stg7 2018", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-configfilename', type=str, default="config.json", help='configuration file name')
    parser.add_argument('--standalone', action='store_true', help="run as standalone version")

    argsdict = vars(parser.parse_args())
    lInfo("read config {}".format(argsdict["configfilename"]))
    # read config file
    try:
        config = json.loads(read_file(os.path.dirname(os.path.realpath(__file__)) + "/" + argsdict["configfilename"]))
    except Exception as e:
        lError("configuration file 'config.json' is corrupt (not json conform). Error: " + str(e))
        return 1

    lInfo("read playlist {}".format(config["playlist"]))

    config["playlist"] = get_and_check_playlist(config["playlist"])

    if config["training"]:
        config["trainingsplaylist"] = get_and_check_playlist(config["trainingsplaylist"])
    else:
        config["trainingsplaylist"] = "" # empty string when no training is set


    if config["voiceRecognition"]:
        # change the rating template to the (radio-) one including voice recognition
        lInfo("Voice recognition active: Automatically loading radio-button template '{}'".format(config["voiceRecognition_template"]))
        config["rating_template"] = config["voiceRecognition_template"]

    if any(system().lower().startswith(i) for i in ["linux", "darwin"]):
        lInfo("Detected *nix-like system; using Linux player command")
        config["player"] = config["player_linux"]  # override player command for linux or macOS

    if argsdict["standalone"]:
        # run server in separate thread
        server_thread = threading.Thread(target=server, args=[config])
        server_thread.start()
        # open (default) web browser
        webbrowser.open("http://127.0.0.1:{port}/".format(port=config["http_port"]), new=1, autoraise=True)
        return

    # default case: run in server mode
    server(config, host='0.0.0.0')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
