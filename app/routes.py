# -*- coding: utf-8 -*-

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Ivan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'Bla bla bla!'
        },
        {
            'author': {'username': 'Sussan'},
            'body': 'The Advengers movies was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
