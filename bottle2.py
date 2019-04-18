# -*- coding: utf-8 -*-
"""
bottle2.py
Created on Wed Apr 17 19:17:26 2019

@author: madhu
"""
from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='.')

run(host='localhost', port=9999)

