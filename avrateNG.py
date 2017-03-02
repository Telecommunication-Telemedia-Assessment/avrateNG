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

# TODO: @auth_basic(check_credentials) should be at every route definition

# TODO: play should not be a route? -> lets discuss about it :)
#@route('/play/:nr')
#@route('/play')
def play(config, video_index):
    video = config["playlist"][video_index]
    lInfo("play {}".format(video))
    shell_call(config["player"].format(filename=video))
    #redirect('/rate')

@route('/')
@auth_basic(check_credentials)
def welcome():
    return template("templates/welcome.tpl", title="AvRate++")

@route('/rate/:video_index')
@route('/rate')
def rate(config, video_index=0):
    video_index = int(video_index)
    play(config, video_index)
    # TODOs:
    #   * would be nice to have somehow a progress bar on rating html page
    #   * survey for name, age .. (demographics and more) should be at the end, and as required part
    #   * at the end there should be a page with "thank you for rating and participating this test..."
    #   * navbar maybe not required, `about` and `avrate++` parts could be integrated small in footer
    return template("templates/rate1.tpl", title="AvRate++", video_index=video_index + 1)

@route('/about')
def about():
    return template("templates/about.tpl", title="AvRate++")


@route('/index')
def index():
    return template("templates/index.tpl", title="AvRate++")

@route('/info')
def info():
    return template("templates/demographicInfo.tpl", title="AvRate++")


@route('/statistics')
def statistics(db):
    # TODO: implement a short diagram of stored ratings, e.g. using http://www.chartjs.org/
    #  or https://developers.google.com/chart/

    # e.g. average rating per video file with confidence intervalls, or something else :)
    return "not yet implemented"


@route('/save_rating/:video_index', method='POST')
@route('/save_rating', method='POST')
def saveRating(db, video_index=0):
    data = request.POST.get('submit')
    # HINT: save everything that is in this submitted formuluar
    # TODO: add timestamp + userid/name of rating to db
    # store : request.POST as json string in database
    db.execute('CREATE TABLE IF NOT EXISTS ratings (video string, rating_filled string);')
    db.execute('INSERT INTO ratings VALUES (?,?);',("1", "dump everything that is in ratings formular to json and store it here"))
    db.commit()
    #print("Submitted value is: "+data)
    redirect('/rate/' + str(video_index))

@route('/save_demographics', method='POST')
def saveDemographics():
    # HINT: save everything that is in this submitted formuluar
    # TODO: ask for these information at the end or beginning of this subjective test
    firstName = request.forms.get("firstName")
    lastName = request.forms.get("lastName")
    age = request.forms.get("age")
    comment = request.forms.get("comment")
    #print("Comment: "+ comment)
    redirect('/info')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./templates/static')


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
