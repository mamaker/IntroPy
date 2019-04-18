# -*- coding: utf-8 -*-
"""
flask1.py
Created on Wed Apr 17 19:17:26 2019
http://localhost:9999
http://localhost:9999/echo/shambhu
@author: madhu
"""
from flask import Flask

app = Flask(__name__,
            static_folder='.',
            static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing

app.run(port=9999, debug=True)

