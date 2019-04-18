# -*- coding: utf-8 -*-
"""
flask3c.py
Created on Wed Apr 17 19:17:26 2019
http://localhost:9999
http://localhost:9999/echo?thing=Gorgo&place=Wilmerding
@author: madhu
"""
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html', **kwargs)

app.run(port=9999, debug=True)

