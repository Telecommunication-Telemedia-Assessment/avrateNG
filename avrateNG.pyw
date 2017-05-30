#!/usr/bin/env python3
import os
import sys
import argparse
import json
import threading
import webbrowser
import time
import datetime
import random

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


def check_credentials(username, password):
    config = ConfigPlugin._config
    validName = config["http_user_name"]
    validPassword = config["http_user_password"]
    return password == validPassword and username == validName


def play(config, video_index, playlist):
    video = config[playlist][video_index]
    lInfo("play {}".format(video))
    shell_call(config["player"].format(filename=video))


@route('/')  # Welcome screen
@auth_basic(check_credentials)
def welcome(db, config):

    # for every new start ("/"): user_id (cookie) is incremented by 1
    if not db.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='ratings'").fetchone():
        user_id = 1 # if ratings table does not exist: first user_id = 1
    else:
        user_id = int(db.execute('SELECT max(user_ID) from ratings').fetchone()[0]) + 1  # new user_ID is always old (highest) user_ID+1
    response.set_cookie("user_id",str(user_id),path="/")

    # initialize session_state variable (throws error when refreshing the page or going back)
    response.set_cookie("session_state","0",path="/")

    # generate new shuffled playlist for every participant when shuffle mode is active
    if config["shuffle"]:
        config["shuffled_playlist"] = random.sample(config["playlist"],len(config["playlist"]))


    # check if training stage is wished and/or training has already finished:
    if config["trainingsplaylist"]: # check if training switch is toggled
        if not request.get_cookie("training_state") == "done": # Cookie that controls if training was already done or is still open
            response.set_cookie("training_state","open",path="/")
            response.set_cookie("training","1",path="/")
            return template("templates/training_welcome.tpl", title="AvRate++", user_id=user_id)
        else:
            response.set_cookie("training","0",path="/")
            return template("templates/welcome.tpl", title="AvRate++", user_id=user_id)
    else:
        response.set_cookie("training","0",path="/")
        return template("templates/welcome.tpl", title="AvRate++", user_id=user_id)


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
            playlist="shuffled_playlist"
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
        response.set_cookie("session_state",str(session_state),path="/")

    return template("templates/rate1.tpl", title="AvRate++", rating_template=config["rating_template"], video_index=video_index, video_count=len(config[playlist]), user_id=user_id)


@route('/about') # About section
@auth_basic(check_credentials)
def about():
    return template("templates/about.tpl", title="AvRate++")


@route('/info') # User Info screen
@auth_basic(check_credentials)
def info():
    return template("templates/demographicInfo.tpl", title="AvRate++")


@route('/finish') # Finish screen
@auth_basic(check_credentials)
def info():
    return template("templates/finish.tpl", title="AvRate++")



@route('/statistics')
@auth_basic(check_credentials)
def statistics(db):

    # Get Data and video names for ratings and transform to JSON objects (better handling)
    db_data=db.execute("SELECT video_name,rating,rating_type from ratings").fetchall()
    video_names = [row[0] for row in db_data]
    rating_data = [int(row[1]) for row in db_data]
    rating_types = [row[2] for row in db_data]
    # extract all kinds of ratings from DB and convert to one dictionary
    rating_dict = {}
    for idx,video in enumerate(video_names):
        rating_dict.setdefault(rating_types[idx], {}).setdefault(video, []).append(rating_data[idx])

    # return dictionary as JSON as interface to Java script (see statistics.tpl file for further info)
    return template("templates/statistics.tpl", title="AvRate++", rating_dict=json.dumps(rating_dict))


@route('/save_rating', method='POST')
@auth_basic(check_credentials)
def saveRating(db,config):  # save rating for watched video

    video_index = request.query.video_index  # extract current video_index from query
    timestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))  # define timestamp
    user_id=int(request.get_cookie("user_id"))

    # Get Mousetracker and write to DB
    if "mouse_track" in request.forms:
        tracker = request.forms["mouse_track"]
        del request.forms["mouse_track"]
    else:
        tracker = "No tracking data submitted."


    # Get POST Data ratings and write to DB
    if len(request.forms.keys()) == 1:
        keys = []
        values = []
        for item in request.forms:
            keys.append(item)
            values.append(request.forms.get(item))
    else:
        lError("The submitted rating form has more than one submitted key/value pair.")

    # Choose DB table to store the ratings
    if not int(request.get_cookie("training")):

        # Lookup the correct playlist
        if config["shuffle"]:
            playlist = "shuffled_playlist"
        else:
            playlist = "playlist"

        video_name = os.path.splitext(os.path.basename(config[playlist][int(video_index)]))[0]

        # Store rating to DB
        db.execute('CREATE TABLE IF NOT EXISTS ratings (user_ID INTEGER, video_ID TEXT, video_name TEXT, rating_type TEXT, rating TEXT, timestamp TEXT);')
        db.execute('INSERT INTO ratings VALUES (?,?,?,?,?,?);',(user_id, video_index, video_name, keys[0], values[0], timestamp))
        db.commit()

        # Store mouse tracking data to DB
        db.execute('CREATE TABLE IF NOT EXISTS tracker (user_ID INTEGER, video_ID TEXT, video_name TEXT, tracker TEXT);')
        db.execute('INSERT INTO tracker VALUES (?,?,?,?);',(user_id, video_index, video_name, tracker))
        db.commit()

    else:
        playlist = "trainingsplaylist"
        video_name = os.path.splitext(os.path.basename(config[playlist][int(video_index)]))[0]

        db.execute('CREATE TABLE IF NOT EXISTS training (user_ID INTEGER, video_ID TEXT, video_name TEXT, rating_type TEXT, rating TEXT, timestamp TEXT);')
        db.execute('INSERT INTO training VALUES (?,?,?,?,?,?);',(user_id, video_index, video_name, keys[0], values[0], timestamp))
        db.commit()

    # check if this was the last video in playlist
    video_index = int(video_index) + 1
    if video_index > len(config[playlist]) - 1:  # playlist over
        if int(request.get_cookie("training")):
            response.set_cookie("training_state","done")
            redirect('/')
        else:
            response.set_cookie("training_state","open")
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
def server_static(filename):
    # needed for routing the static files (CSS)
    this_dir_path = os.path.dirname(os.path.abspath(__file__))
    return static_file(filename, root=this_dir_path + '/templates/static')


def server(config, host="127.0.0.1"):
    install(SQLitePlugin(dbfile='ratings.db'))
    install(ConfigPlugin(config))

    lInfo("server starting.")
    run(host=host, port=config["http_port"], debug=True, reloader=True)
    lInfo("server stopped.")


def main(params=[]):
    parser = argparse.ArgumentParser(description='avrate++', epilog="stg7 2017", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-configfilename', type=str, default="config.json", help='configuration file name')
    parser.add_argument('-playlist', type=str, default="playlist.list", help='video sequence play list')
    parser.add_argument('--standalone', action='store_true', help="run as standalone version")
    parser.add_argument('-trainingsplaylist', type=str, default="", help='playlist for training session. If none is given: No training')
    parser.add_argument('-shuffle', action='store_true', help='Set, when playlist should be randomized')
    parser.add_argument('-voiceRecognition', action='store_true', help='Set, when selection should be made using voice recognition')

    argsdict = vars(parser.parse_args())
    lInfo("read config {}".format(argsdict["configfilename"]))
    # read config file
    try:
        config = json.loads(read_file(os.path.dirname(os.path.realpath(__file__)) + "/" + argsdict["configfilename"]))
    except Exception as e:
        lError("configuration file 'config.json' is corrupt (not json conform). Error: " + str(e))
        return 1

    lInfo("read playlist {}".format(argsdict["playlist"]))
    with open(argsdict["playlist"]) as playlistfile:
        playlist = [os.path.join(*x.strip().split("/")) for x in playlistfile.readlines() if x.strip() != ""]
        config["playlist"] = playlist  # add cleaned playlist to config
        # check if each video exists
        for video in playlist:
            if not os.path.isfile(video):
                lError("'{}' is not a valid videofile, please check your playlistfile".format(video))
                return -1


    if argsdict["trainingsplaylist"]:
        lInfo("read playlist for Training stage {}".format(argsdict["trainingsplaylist"]))
        with open(argsdict["trainingsplaylist"]) as trainingsplaylistfile:
            trainingsplaylist = [os.path.join(*x.strip().split("/")) for x in trainingsplaylistfile.readlines() if x.strip() != ""]
            config["trainingsplaylist"] = trainingsplaylist  # add cleaned playlist to config
            # check if each video exists
            for video in trainingsplaylist:
                if not os.path.isfile(video):
                    lError("'{}' is not a valid videofile, please check your playlistfile".format(video))
                    return -1
    else:
        config["trainingsplaylist"] = "" # empty string when no training is set


    if argsdict["shuffle"]:
        # easiest way: create shuffled temporary playlist and point to it instead of normal playlist (nothing else needs to be changed)
        lInfo("shuffle mode active")
        config["shuffle"] = True
    else:
        config["shuffle"] = False

    if argsdict["voiceRecognition"]:
        # change the rating template to the (radio-) one including voice recognition
        lInfo("Voice recognition active: Automatically loading radio-button template '{}'".format(config["voiceRecognition_template"]))
        config["rating_template"] = config["voiceRecognition_template"]


    from sys import platform
    if platform == "linux" or platform == "linux2":
        config["player"] = config["player_linux"]  # override player command for linux

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
