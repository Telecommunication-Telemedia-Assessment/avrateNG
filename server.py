#!/usr/bin/env python3
import os
import sys
import argparse
import json

# load libs from lib directory
import loader
from log import *
from system import *

from bottle import Bottle
from bottle import auth_basic
from bottle import route
from bottle import run
from bottle import template
from bottle import request
from bottle import redirect
from bottle import response
from bottle import error
from bottle import static_file


#@route('/play/:nr')
@route('/play')
def play():
    os.system("sleep 20")
    return template("templates/play.tpl", title="AvRate++")


@route('/about')
def about():
    return template("templates/about.tpl", title="AvRate++")

@route('/')
def index():
    return template("templates/index.tpl", title="AvRate++")


def main(params):

    # TODO(stg7) change to external config file
    config = {}
    config["webport"] = 12345


    lInfo("server starting.")
    run(host='0.0.0.0', port=config["webport"], debug=True, reloader=True)
    lInfo("server stopped.")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))