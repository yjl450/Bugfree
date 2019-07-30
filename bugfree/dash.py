#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: 2019/07/28
# Project: BugFree

'''
    This script handles the content of dashboard
'''

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import pymysql
import tushare
from bugfree.db import get_db, get_cursor

bp = Blueprint('dash', __name__)

@bp.route('/dash')
def dash():
    """
    :return: Dashboard Page
    """
    title = 'InfoMobile - Dashboard'
    return render_template('dash/dash.html', title=title)

@bp.route('/design/index')
def navi():
    """
    :return: Navigation template
    """
    login_flag = False
    title = 'Index template'
    return render_template('index/init.html', login_flag = login_flag, title = title)