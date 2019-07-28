#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: 2019/07/27
# Project: BugFree

'''
    This script handles the all the basic templates
'''

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import pymysql
# from bugfree.db import get_db, get_cursor

bp = Blueprint('design', __name__)

@bp.route('/design')
def design():
    """
    :return: Navigation template
    """
    return """<a href="design/index">index</a><br><a href="design/basic">dash navi</a><br><a href="design/dash">dash</a><br>"""

@bp.route('/design/index')
def navi():
    """
    :return: Navigation template
    """
    login_flag = True
    title = 'Index template'
    return render_template('index/init.html', login_flag = login_flag, title = title)

@bp.route('/design/dash')
def dash_design():
    """
    :return: Navigation template
    """
    login_flag = True
    title = 'dashboard template'
    return render_template('dash/dash.html', login_flag = login_flag, title = title)

@bp.route('/design/basic')
def navi_dash():
    """
    :return: Navigation template
    """
    login_flag = True
    title = 'navi template'
    return render_template('dash/basic.html', login_flag = login_flag, title = title)