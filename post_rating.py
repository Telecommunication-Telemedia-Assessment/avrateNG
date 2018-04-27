#!/usr/bin/env python3
"""
    post rating script

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
    db.execute('INSERT INTO feedback VALUES (?,?);', (user_id, json.dumps(dict(request.forms))))
    db.commit()

    redirect('/finish')
