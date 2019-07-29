#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: 2019/07/26
# Project: BugFree

'''
    This script handles the index page, login, and registration
'''
import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import pymysql
from bugfree.db import get_db, get_cursor

bp = Blueprint('index', __name__)

secu = ['What was the house number and street name you lived in as a child?', 'What were the last four digits of your childhood telephone number?', 'What primary school did you attend?', 'In what town or city was your first full time job?', 'In what town or city did you meet your spouse/partner?',
        'What is the middle name of your oldest child?', "What are the last five digits of your driver's licence number?", "What is your grandmother's (on your mother's side) maiden name?", "What is your spouse or partner's mother's maiden name?", 'In what town or city did your mother and father meet?', 'What time of the day were you born? (hh:mm)']


@bp.route('/')
def index():
    """
    :return: Index Page
    """
    title = 'InfoMobile - Welcome'
    return render_template('index/index.html', title=title)


@bp.route('/reg', methods=('GET', 'POST'))
def reg():
    """
    :return: Registration Page
    """

    error = None
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        pwd = request.form['pwd']
        question = request.form['question']
        answer = request.form['answer']
        cursor.execute('SELECT * from user WHERE email = %s',(email,))  # Fetch user info
        if cursor.fetchone() is not None:
            error = 'User with e-mail {} already exists'.format(email)
        else:
            try:
                cursor.execute("INSERT INTO user (name, email, pwd, question, answer) values(%s, %s, %s, %s, %s)", (user, email, pwd, question, answer))
                db.commit()
                return redirect(url_for('index.confirm_reg', user=user, email=email))
            except pymysql.Error as e:
                    db.rollback()  # if register not successful then rollback
                    error = e.args[1]
        flash(error)

    title = 'InfoMobile - Register'
    return render_template('index/reg.html', title=title, question_list=secu)

@bp.route('/reg/confirm')
def confirm_reg():
    title = 'InfoMobile - Registration Complete'
    return render_template('index/reg_confirm.html', user='user', email='a@a', title = title)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """
    :return: Login Page
    """

    error = None
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pwd']
        try:
            keep = request.form['keep']
        except:
            keep = None
        cursor.execute('SELECT name, email, pwd from user WHERE email = %s',(email,))
        user = cursor.fetchone()
        if user is None:
            error = "User does not exist"
        elif pwd != user[2]:
            error = "Incorrect e-mail or password"
        if error is None:
            session.clear()
            if keep is not None:
                session.permanent = True
            session['name'] = user[0]
            session['email'] = user[1]
            return redirect(url_for('dash.dash'))
        flash(error)
         
    title = 'InfoMobile - Sign In'
    return render_template('index/login.html', title=title)

@bp.before_app_request
def load_logged_in_user():
    session_name = session.get('name')
    if session_name is None:
        g.login_flag = False
    else:
        g.login_flag = True
        g.name = session_name
        g.email = session.get('email')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.index'))

@bp.errorhandler(404)
def page_not_found():
    """
    Deal with error code 404
    :return: redirect to index page
    """
    pass
