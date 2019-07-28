#!/user/bin/env/python3
# -*- coding: utf-8 -*-
# Author: Helium Liu
# @Time: 2019/07/28
# Project: BugFree

'''
    This script handles database related functions.
'''

import pymysql
from flask import current_app, g
from flask.cli import with_appcontext
import click

def init_app(app):
    """
    Register function when app launches.
    
    Args:
        None.    
    Returns:
        None.
    """
    
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db():
    """
    This function connects to database.
    
    Args:
        None   
    Returns:
        Database object.
    """

    if 'db' not in g:
        g.db = pymysql.connect(
            host="localhost", # host
            user="root_power", # username
            password="Bugfree2019", # password
            db="bf" # database name
            )
    return g.db

def get_cursor():
    """
    Return the cursor of the current database.
    
    Args:
        None.
    Returns:
        pymysql cursor.
    """
    
    if 'db' not in g:
        db = get_db()
        return db.cursor()
    return g.db.cursor()
    
# create cursor

def init_db():
    """
    This function initialize the database.
    
    Args:
        None.    
    Returns:
        None.
    """
    cursor = get_cursor()
    with current_app.open_resource('db/bf.sql') as f:
        queries = str(f.read(), 'utf-8').split(';')[:-1]
        for query in queries:
            cursor.execute(query)

def execute_sql(filename):
    """
    This funcition execute the SQL file using pymysql as a whole.
    
    Args:
        filename: filename.
    
    Returns:
        retval: indicates whether the execution is successful. If it is, return 
        True, else False.
    """
    cursor = get_cursor()
    with open(filename, 'rb') as f:
        queries = str(f.read(), 'utf-8').split(';')[:-1]
        for query in queries:
            cursor.execute(query)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    """
    Clear existing data and create new tables. Insert certain test data. Echo 'Database Initialized' if succeeded.
    
    Args:
        None.    
    Returns:
        None.
    """
    init_db()
    click.echo('Database Initialized')
    
def close_db(e=None):
    """
    Close database connection.
    
    Args:
        e: event. Default none.    
    Returns:
        None
    """
    db = g.pop('db',None)
    if db is not None:
        db.close()

    