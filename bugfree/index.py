#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: 2019/07/26
# Project: BugFree

'''
    This script handles the index page, login, and registration
'''

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import pymysql
# from bgfe.db import get_db, get_cursor

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    """
    :return: Index Page
    """
    login_flag = False
    title = 'InfoMobile - Welcome'
    return render_template('index/index.html', login_flag = login_flag, title = title)

@bp.route('/reg', methods=('GET', 'POST'))
def reg():
    """
    :return: Registration Page
    """
    login_flag = False
    title = 'InfoMobile - Register'
    return render_template('index/reg.html', login_flag = login_flag, title = title)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """
    :return: Login Page
    """
    login_flag = False
    title = 'InfoMobile - Sign In'
    return render_template('index/login.html', login_flag = login_flag, title = title)

@bp.errorhandler(404)
def page_not_found():
    """
    Deal with error code 404
    :return: redirect to index page
    """
    pass