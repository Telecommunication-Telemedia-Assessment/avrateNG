#!/usr/bin/env python3
"""
    AVRateNG main script

    This file is part of AVRateNG.
    AVRateNG is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    AVRateNG is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with AVRateNG.  If not, see <http://www.gnu.org/licenses/>.
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


def check_credentials(username, password):
    """
    check user/password to run the test,
    this is only required if AVRateNG is started on a computer in
    an opem accessible network, because network ports are opened,
    such an open network configuration should be avoided running a test.
    """
    config = ConfigPlugin._config
    validName = config["http_user_name"]
    validPassword = config["http_user_password"]
    return password == validPassword and username == validName


@route("/play/<stimuli_idx>")
@auth_basic(check_credentials)
def play(db, config, stimuli_idx):
    """
    play a given media file by its index inside the playlist
    """
    stimuli_idx = int(stimuli_idx)
    print("play", stimuli_idx)

    user_id, playlist_idx = get_user_id_playlist(db, config)
    if int(request.get_cookie("training")):
        stimuli_file = config["trainingsplaylist"][stimuli_idx]
    else:
        stimuli_file = config["playlist"][playlist_idx[stimuli_idx]]

    print(stimuli_file)
    if config.get("no_media_playback", False):
        return

    def q(x):
        """ quote the media name for command line usage,
        prevends problems with spaces in media filenames"""
        return "\"" + x + "\""
    stimuli_file = " ".join(map(q, stimuli_file))

    lInfo("play {}".format(stimuli_file))
    if "gray_video" in config:
        stimuli_file = q(config["gray_video"]) + " " + stimuli_file + " " + q(config["gray_video"])
        lInfo("use gray video before and after: {}".format(stimuli_file))
    lInfo("player command")
    print(config["player"].format(filename=stimuli_file))
    shell_call(config["player"].format(filename=stimuli_file))



def get_user_id_playlist(db, config):
    if request.get_cookie("user_id"):
        user_id = int(request.get_cookie("user_id"))
        playlist = json.loads(db.execute('SELECT playlist from user_playlist where user_ID==? ;', (user_id,)).fetchone()[0])
        return user_id, playlist
    """ read user id from database """
    if not db.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='ratings'").fetchone():
        user_id = 1 # if ratings table does not exist: first user_id = 1
    else:
        user_id = int(db.execute('SELECT max(user_ID) from ratings').fetchone()[0]) + 1  # new user_ID is always old (highest) user_ID+1

    playlist = [x for x in range(len(config["playlist"]))]
    if config["shuffle"]:
        random.shuffle(playlist)
    #playlist = playlist[0:config["max_stimuli"]]

    db.execute('CREATE TABLE IF NOT EXISTS user_playlist (user_ID INTEGER PRIMARY KEY, playlist TEXT, timestamp TEXT);')
    db.execute('INSERT INTO user_playlist VALUES (?,?,?);',(user_id, json.dumps(playlist), create_timestamp()))

    # here the current user id is included in the ratings table,
    # to make sure that it is not used by anyone else
    db.execute('CREATE TABLE IF NOT EXISTS ratings (user_ID INTEGER, stimuli_ID TEXT, stimuli_file TEXT, rating_type TEXT, rating TEXT, timestamp TEXT);')
    db.execute('INSERT INTO ratings VALUES (?,?,?,?,?,?);',(user_id, -1, "", "user_registered", -1, create_timestamp()))
    db.commit()
    return user_id, playlist


@route('/')  # Welcome screen
@auth_basic(check_credentials)
def welcome(db, config):
    """
    welcome screen
    """
    user_id, playlist = get_user_id_playlist(db, config)

    response.set_cookie("user_id", str(user_id), path="/")

    # initialize session_state variable (throws error when refreshing the page or going back)
    response.set_cookie("session_state", "0", path="/")
    response.set_cookie("stimuli_done", "0", path="/")
    response.set_cookie("training", "0", path="/")

    # check if training stage is wished and/or training has already finished:
    if config["trainingsplaylist"]: # check if training switch is toggled
        if not request.get_cookie("training_state") == "done": # Cookie that controls if training was already done or is still open
            response.set_cookie("training_state","open", path="/")
            response.set_cookie("training", "1", path="/")

    return template(
        config["template_folder"] + "/welcome.tpl",
        title="AVRateNG",
        user_id=user_id
    )


@route('/start_test')
def start_test(config, db):
    response.set_cookie("training", "0", path="/")
    response.set_cookie("training_state", "done", path="/")
    return template(
        config["template_folder"] + "/start_test.tpl",
        title="AVRateNG"
    )


@route('/training/<stimuli_idx>')
@route('/training/<stimuli_idx>', method="POST")
def training(config, db, stimuli_idx):

    user_id = int(request.get_cookie("user_id"))
    stimuli_idx = int(stimuli_idx)

    if len(config["trainingsplaylist"]) == 0:
        redirect('/rate/0')
        return
    if stimuli_idx >= len(config["trainingsplaylist"]):
        redirect('/start_test')
        return
    return bottle.template(
        config["template_folder"] + "/rate.tpl",
        title="AVRateNG",
        train=True,
        rating_template=config["rating_template"],
        stimuli_done=stimuli_idx,
        stimuli_idx=stimuli_idx,
        stimuli_file=config["trainingsplaylist"][stimuli_idx],
        stimuli_count=len(config["trainingsplaylist"]),
        user_id=user_id,
        question=config.get("question", "add question to config.json"),
        dev=request.get_cookie("dev") == "1"
    )


@route('/rate/<stimuli_idx>')  # Rating screen with stimuli_idx as variable
@auth_basic(check_credentials)
def rate(db, config, stimuli_idx):
    """
    show rating screen for one specific stimuli
    """
    stimuli_idx = int(stimuli_idx)

    user_id, playlist_idx = get_user_id_playlist(db, config)

    session_state = int(request.get_cookie("session_state"))
    stimuli_done = int(request.get_cookie("stimuli_done"))

    # Select correct playlist for lookup
    if int(request.get_cookie("training")):
        playlist = "trainingsplaylist"
    else:
        playlist = "playlist"

    # Check if video should be played or was already watched
    if stimuli_idx == session_state:
        play_video = 1
    else:
        play_video = 0

    # play video only on first visit
    if play_video == 1:
        # play(config, stimuli_idx, playlist)  # the play call (via the play route) is moved to the rating template
        # play just one time
        play_video = 0
        session_state = session_state + 1
        response.set_cookie("session_state", str(session_state), path="/")

    return template(
        config["template_folder"] + "/rate.tpl",
        title="AVRateNG",
        rating_template=config["rating_template"],
        stimuli_idx=stimuli_idx,
        stimuli_file=config["playlist"][stimuli_idx],
        stimuli_done=stimuli_done,
        stimuli_count=len(config[playlist]),
        user_id=user_id,
        question=config.get("question", "add question to config.json"),
        dev=request.get_cookie("dev") == "1"
    )


@route('/questionnaire')
@auth_basic(check_credentials)
def questionnaire(config):
    """
    show questionnaire if required
    """
    if not config.get("questionnaire", True):
        if int(request.get_cookie("training")) > 0:
            redirect('/training/0')
            return
        return redirect('/rate/0')
    return template(
        config["template_folder"] + "/questionnaire.tpl",
        title="AVRateNG",
        user_id=request.get_cookie("user_id"),
        dev=request.get_cookie("dev") == "1"
    )

@route('/questionnaire', method='POST')
@auth_basic(check_credentials)
def questionnaire_save(db, config):
    """
    saves demographic info into sqlite3 table,
    all user information (user_id is key in tables) are stored as JSON string
    """
    user_id = int(request.get_cookie("user_id"))

    db.execute('CREATE TABLE IF NOT EXISTS info (user_ID, info_json TEXT);')
    db.execute('INSERT INTO info VALUES (?,?);',(user_id, json.dumps(dict(request.forms))))
    db.commit()
    if int(request.get_cookie("training")) > 0:
        redirect('/training/0')
        return
    redirect('/rate/0')


@route('/finish')  # Finish screen
@auth_basic(check_credentials)
def finish(config):
    """
    will be shown after test was completly done
    """
    return template(config["template_folder"] + "/finish.tpl", title="AVRateNG")


@route('/save_rating', method='POST')
@auth_basic(check_credentials)
def save_rating(db, config):
    """
    save rating for watched stimuli
    """
    stimuli_idx = request.query.stimuli_idx  # extract current stimuli_idx from query
    timestamp = create_timestamp()

    user_id = int(request.get_cookie("user_id"))
    stimuli_done = int(request.get_cookie("stimuli_done")) + 1
    response.set_cookie("stimuli_done", str(stimuli_done), path="/")

    # get POST data ratings and write to DB
    request_data_pairs = {}
    for item in request.forms:
        request_data_pairs[item] = request.forms.get(item)

    stimuli_ID = request_data_pairs["stimuli_idx"]
    stimuli_file = request_data_pairs["stimuli_file"]
    excluded = ["stimuli_idx", "stimuli_file"]

    db.execute('CREATE TABLE IF NOT EXISTS ratings (user_ID INTEGER, stimuli_ID TEXT, stimuli_file TEXT, rating_type TEXT, rating TEXT, timestamp TEXT);')

    for item in filter(lambda x: x not in excluded , request_data_pairs):
        db.execute(
            'INSERT INTO ratings VALUES (?,?,?,?,?,?);',
            (user_id, stimuli_ID, stimuli_file, item, request_data_pairs[item], timestamp)
        )

    db.commit()

    if stimuli_done >= len(config["playlist"]):
        redirect('/finish')

    redirect('/rate/' + str(stimuli_done))



@route('/static/<filename:path>',name='static')  # access the stylesheets and static files (JS files,...)
@auth_basic(check_credentials)
def server_static(filename,config):
    """
    needed for routing the static files (CSS)
    """
    this_dir_path = os.path.dirname(os.path.abspath(__file__))
    return static_file(filename, root=this_dir_path + '/'+ config["template_folder"]  +'/static')


def server(config, host="127.0.0.1"):
    """
    start the server part of AVRateNG
    """
    install(SQLitePlugin(dbfile='ratings.db'))
    install(ConfigPlugin(config))
    dev = config["development"]
    lInfo("server starting. devmode: " + str(dev))
    if dev:
        run(
            host=host,
            port=config["http_port"],
            debug=True,
            reloader=True,
            fast=True
        )
    else:
        run(
            host=host,
            port=config["http_port"],
            debug=False,
            reloader=False,
            fast=False
        )
    lInfo("server stopped.")


@route('/reset_cookies')
@route('/rc')
@auth_basic(check_credentials)
def reset_cookies(db, config):
    """
    perfrom a reset of the cookies, this is only for internal usage,
    in case AVRateNG needs to be resetted
    """
    for cookie in request.cookies:
        response.set_cookie(cookie, '', expires=0)
    redirect('/')

@route('/dev')
def dev(db, config):
    """
    development mode
    """
    response.set_cookie("dev", "1", path="/")
    redirect('/')


def create_timestamp():
    return str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S %f'))  # define timestamp


def get_and_check_playlist(playlistfilename):
    """
    reads playlist and checks if files are existing,
    otherwise an error is shown
    """
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
    parser = argparse.ArgumentParser(
        description='AVRateNG',
        epilog="stg7 2023",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-configfilename', type=str, default="config.json", help='configuration file name')
    parser.add_argument('--standalone', action='store_true', help="run as standalone version")
    parser.add_argument('--development', '-d', action='store_true', help="run in dev mode")

    argsdict = vars(parser.parse_args())
    lInfo("read config {}".format(argsdict["configfilename"]))
    # read config file
    try:
        config = json.loads(read_file(os.path.dirname(os.path.realpath(__file__)) + "/" + argsdict["configfilename"]))
    except Exception as e:
        lError("configuration file 'config.json' is corrupt (not json conform). Error: " + str(e))
        return 1
    config["development"] = argsdict["development"]
    lInfo("read playlist {}".format(config["playlist"]))

    config["playlist"] = get_and_check_playlist(config["playlist"])

    if config["training"]:
        config["trainingsplaylist"] = get_and_check_playlist(config["trainingsplaylist"])
    else:
        config["trainingsplaylist"] = None # no training is set

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
