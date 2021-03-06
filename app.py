# -*- coding: utf-8 -*-

# Imports
from flask import (Flask, render_template, request, redirect, jsonify,
                   url_for, flash)

from flask import session as login_session
import random
import string

import json
from flask import make_response
import requests
import os

app = Flask(__name__)

# Web Page #1 - Homepage - Website homepage
@app.route('/')
@app.route('/home')
def showHomepage():
    return render_template('homepage.html')

# Web Page #2 - Article1 - First article 
@app.route('/article1')
def showArticle1():
    return render_template('article1.html')

# Web Page #3 - Article1 - First article 
@app.route('/article2')
def showArticle2():
    return render_template('article2.html')

# Web Page #4 - Article1 - First article 
@app.route('/article3')
def showArticle3():
    return render_template('article3.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)