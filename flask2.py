# -*- coding: utf-8 -*-
"""
flask2.py
Created on Wed Apr 17 19:17:26 2019
http://localhost:9999
http://localhost:9999/echo/shambhu
@author: madhu
"""
from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

app.run(port=9999, debug=True)

