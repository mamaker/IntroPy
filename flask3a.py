# -*- coding: utf-8 -*-
"""
flask3a.py
Created on Wed Apr 17 19:17:26 2019
http://localhost:9999
http://localhost:9999/echo/shambhu/chanda
@author: madhu
"""
from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
    return render_template('flask3.html', thing=thing, place=place)

app.run(port=9999, debug=True)

