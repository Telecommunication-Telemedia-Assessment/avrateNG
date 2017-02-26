#!/usr/bin/env python3
import os
import sys
import argparse
import json

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
from bottle.ext import sqlite

config = None

def check_credentials(username, password):
    validName = config["http_user_name"]
    validPassword = config["http_user_password"]
    if password == validPassword and username == validName:
        return True
    return False

# TODO: @auth_basic(check_credentials) should be at every route definition

#@route('/play/:nr')
@route('/play')
def play():
    video = config["playlist"][0]  # TODO: somehow get current video index
    lInfo("play {}".format(video))
    shell_call(config["player"].format(filename=video))
    #redirect('/rate')

@route('/')
@auth_basic(check_credentials)
def welcome():
    return template("templates/welcome.tpl", title="AvRate++")

@route('/rate')
def rate():
    play()
    # TODOs:
    #   * would be nice to have somehow a progress bar on rating html page
    #   * survey for name, age .. (demographics and more) should be at the end, and as required part
    #   * at the end there should be a page with "thank you for rating and participating this test..."
    #   * navbar maybe not required, `about` and `avrate++` parts could be integrated small in footer
    return template("templates/rate1.tpl", title="AvRate++")

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
    return "not yet implemented"

@route('/save_rating', method='POST')
def saveRating(db):
    data = request.POST.get('submit')
    # HINT: save everything that is in this submitted formuluar
    # TODO: add timestamp + userid/name of rating to db
    db.execute('CREATE TABLE IF NOT EXISTS ratings (video string, rating_filled string);')
    db.execute('INSERT INTO ratings VALUES (?,?);',("1", "dump everything that is in ratings formular to json and store it here"))
    db.commit()
    #print("Submitted value is: "+data)
    redirect('/rate')

@route('/save_demographics', method='POST')
def saveDemographics():
    # HINT: save everything that is in this submitted formuluar
    firstName = request.forms.get("firstName")
    lastName = request.forms.get("lastName")
    age = request.forms.get("age")
    comment = request.forms.get("comment")
    #print("Comment: "+ comment)
    redirect('/info')


@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./templates/static')


def main(params):
    parser = argparse.ArgumentParser(description='avrate++', epilog="stg7 2017", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-configfilename', type=str, default="config.json", help='configuration file name')
    parser.add_argument('-playlist', type=str, default="playlist.list", help='video sequence play list')

    argsdict = vars(parser.parse_args())
    lInfo("read config {}".format(argsdict["configfilename"]))
    # read config file
    global config
    try:
        config = json.loads(read_file(os.path.dirname(os.path.realpath(__file__)) + "/" + argsdict["configfilename"]))
    except Exception as e:
        lError("configuration file 'config.json' is corrupt (not json conform). Error: " + str(e))
        return 1

    with open(argsdict["playlist"]) as playlistfile:
        playlist = [os.path.join(*x.strip().split("/")) for x in playlistfile.readlines() if x.strip() != ""]
        config["playlist"] = playlist
        for video in playlist:
            if not os.path.isfile(video):
                lError("'{}' is not a valid videofile, please check your playlistfile".format(video))
                return -1

    from sys import platform
    if platform == "linux" or platform == "linux2":
        # linux
        config["player"] = config["player_linux"]


    plugin = sqlite.Plugin(dbfile='ratings.db')
    install(plugin)

    lInfo("server starting.")
    run(host='0.0.0.0', port=config["http_port"], debug=True, reloader=True)
    lInfo("server stopped.")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
