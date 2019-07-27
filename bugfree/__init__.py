#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: 2019/07/26
# Project: BugFree

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # Change to random number when deploy
        DATABASE=os.path.join(app.instance_path, 'bugfree.sql'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register design blueprint
    # Responsible for template development
    from . import design
    app.register_blueprint(design.bp)

    # Register index blueprint
    # Responsible for index page, registration, and login.
    from . import index
    app.register_blueprint(index.bp)



    return app