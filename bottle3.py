# -*- coding: utf-8 -*-
"""
bottle3.py
Created on Wed Apr 17 19:17:26 2019
http://localhost:9999
http://localhost:9999/echo/shambhu
@author: madhu
"""
from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say Hello to my little friend: %s!" % thing

run(host='localhost', port=9999)

