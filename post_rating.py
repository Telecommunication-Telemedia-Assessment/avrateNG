#!/usr/bin/env python3
from avrateNG import *

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



@route('/feedback') # User Info screen
@auth_basic(check_credentials)
def feedback():
    return template("templates/feedback.tpl", title="AvRate++")


@route('/save_feedback', method='POST')
@auth_basic(check_credentials)
def saveFeedback(db, config):  # save user information (user_id is key in tables) as JSON string
    user_id = int(request.get_cookie("user_id"))

    db.execute('CREATE TABLE IF NOT EXISTS feedback (user_ID, feedback_json TEXT);')
    db.execute('INSERT INTO info VALUES (?,?);', (user_id, json.dumps(dict(request.forms))))
    db.commit()

    redirect('/finish')
