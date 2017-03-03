#!/usr/bin/env python3
import os
import sys
import argparse
import json
import threading
import webbrowser

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

# todo: verhinden dass der nutzer "aktualisieren" im browser drücken kann, weil sonst das video abspielen wiederholt werden kann

def check_credentials(username, password):
    config = ConfigPlugin._config
    validName = config["http_user_name"]
    validPassword = config["http_user_password"]
    if password == validPassword and username == validName:
        return True
    return False




def play(config, video_index):
    video = config["playlist"][video_index]
    lInfo("play {}".format(video))
    shell_call(config["player"].format(filename=video))
    #redirect('/rate')

@route('/')
@auth_basic(check_credentials)
def welcome():
    return template("templates/welcome.tpl", title="AvRate++")

user_id = 0 # initialize user (starts over for each new browser session)

@route('/rate/<video_index>')
@auth_basic(check_credentials)
def rate(config, video_index):
    video_index = int(video_index)
    play(config, video_index)
    if video_index == 0:
        global user_id 
        user_id = user_id + 1
    # Todo: So far, user_id is a global variable which increments on every routing to rate/0 (meaning on every first video item). Also it resets to 1 every time the script starts over -> Better way?
    return template("templates/rate1.tpl", title="AvRate++", video_index=video_index, video_count=len(config["playlist"]))


@route('/about')
@auth_basic(check_credentials)
def about():
    return template("templates/about.tpl", title="AvRate++")


@route('/index')
@auth_basic(check_credentials)
def index():
    return template("templates/index.tpl", title="AvRate++")

@route('/info')
@auth_basic(check_credentials)
def info():
    return template("templates/demographicInfo.tpl", title="AvRate++")

@route('/finish')
@auth_basic(check_credentials)
def info():
    return template("templates/finish.tpl", title="AvRate++")



@route('/statistics')
@auth_basic(check_credentials)
def statistics(db):
    # TODO: implement a short diagram of stored ratings, e.g. using http://www.chartjs.org/
    #  or https://developers.google.com/chart/

    # e.g. average rating per video file with confidence intervalls, or something else :)
    return "not yet implemented"


@route('/save_rating', method='POST')
@auth_basic(check_credentials)
def saveRating(db,config):
    #data = request.POST.get('submit')
    # HINT: save everything that is in this submitted formuluar
    # TODO: add timestamp + userid/name of rating to db
    # store : request.POST as json string in database
    db.execute('CREATE TABLE IF NOT EXISTS ratings (video string, rating_filled string);')
    db.execute('INSERT INTO ratings VALUES (?,?);',("1", "dump everything that is in ratings formular to json and store it here"))
    db.commit()
    video_index = request.query.video_index
    video_index=int(video_index) + 1
    if video_index > len(config["playlist"])-1:
        redirect('/info')
    else:
        redirect('/rate/' + str(video_index))
    

@route('/save_demographics', method='POST')
@auth_basic(check_credentials)
def saveDemographics():
    # HINT: save everything that is in this submitted formuluar
    firstName = request.forms.get("firstName")
    lastName = request.forms.get("lastName")
    age = request.forms.get("age")
    comment = request.forms.get("comment")
    #print("Comment: "+ comment)
    redirect('/finish')


@route('/static/<filename>')
@auth_basic(check_credentials)
def server_static(filename):
    return static_file(filename, root='/templates/static')


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

    from sys import platform
    if platform == "linux" or platform == "linux2":
        config["player"] = config["player_linux"]  # override player command for linux

    if argsdict["standalone"]:
        # run server in separate thread
        server_thread = threading.Thread(target=server, args=[config])
        server_thread.start()
        # open (default) web browser
        # TODO: think about a separate browser instanciation, e.g. chrome without close button and tabs?
        # TODO: maybe deactivate password authentification if avrate++ runs in standalone mode?
        webbrowser.open("http://127.0.0.1:{port}/".format(port=config["http_port"]), new=1, autoraise=True)
        return

    # default case: run in server mode
    server(config, host='0.0.0.0')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
