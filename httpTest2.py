# -*- coding: utf-8 -*-
"""
httpTest2.py
Created on Wed Apr 17 16:09:46 2019

@author: madhu
"""
import requests


url = 'http://www.omdbapi.com'
#url = 'http://www.omdbapi.com/?apikey=FF68a35f&t=eegah&y=1962'
myapikey = 'FF68a35f'
#title = input ('Type a movie Title:')
title = 'jaws'
args = {'apikey': myapikey, 't': title}
try:
    print('*'*30)
    print(url)
    resp = requests.get(url, params=args)
    print(resp)
    print('*'*30)
    
    the_status = resp.status_code
    print('HTTP Status code:', the_status)
    if the_status in range(200,300):
        print('*'*30)
        js_data = resp.json()
        print('*'*30)
        print(js_data)
        print('*'*30)
        print('Title :', js_data['Title'])
        print('*'*30)
        print('plot :', js_data['Plot'])
        print('*'*30)
        print('Headers:')
        for hdr in resp.headers:
            print(hdr, type(hdr))
        print('*'*30)
    
    
except:
    print('Sorry, Error accessing url', url)    