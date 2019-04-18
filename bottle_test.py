# -*- coding: utf-8 -*-
"""
bottle_test.py
Created on Wed Apr 17 19:17:26 2019

@author: madhu
"""
import requests

resp = requests.get('http://localhost:9999/echo/Mothra')
if resp.status_code == 200 and \
    resp.text == 'Say Hello to my little friend: Mothra!':
    print('It worked! That almost never happens!')
else:
    print('Argh, got this:', resp.text)