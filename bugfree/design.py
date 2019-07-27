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
# from bgfe.db import get_db, get_cursor

bp = Blueprint('design', __name__)

@bp.route('/design')
def design():
    """
    :return: Navigation template
    """
    return """<a href="design/index">index</a>"""

@bp.route('/design/index')
def navi():
    """
    :return: Navigation template
    """
    login_flag = False
    title = 'Index template'
    return render_template('index/init.html', login_flag = login_flag, title = title)