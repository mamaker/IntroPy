# -*- coding: utf-8 -*-
"""
bottle1.py
Created on Wed Apr 17 19:17:26 2019

@author: madhu
"""
from bottle import route, run
@route('/')
def home():
    return "It isn't fancy, but it's my home page"
run(host='localhost', port=9999)

