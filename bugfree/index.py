#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: $ {
# @Time: $ {DATE} $ {TIME}
# Project: BugFree

'''
    This script handles the index page, login, and registration
'''

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import pymysql
# from bgfe.db import get_db, get_cursor

bp = Blueprint('index', __name__)

@bp.route('/design/index')
def navi():
    """
    :return: Navigation template
    """
    login_flag = False
    title = 'Index template'
    return render_template('index/init.html', login_flag = login_flag, title = title)

@bp.route('/')
def index():
    """
    :return: Index Page
    """
    login_flag = True
    title = 'Welcome to Bugfree'
    return render_template('index/index.html', login_flag = login_flag, title = title)

@bp.route('/reg')
def reg():
    """
    :return: Registration Page
    """
    login_flag = False
    title = 'Welcome to Bugfree'
    return render_template('index/reg.html', login_flag = login_flag, title = title)

@bp.route('/login')
def login():
    """
    :return: Login Page
    """
    login_flag = False
    title = 'Welcome to Bugfree'
    return render_template('index/login.html', login_flag = login_flag, title = title)

# @bp.errorhandler(404)
# def page_not_found():
#     """
#     Deal with error code 404
#     :return: redirect to index page
#     """
#     pass