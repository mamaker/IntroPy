# -*- coding: utf-8 -*-
"""
httpTest.py
Created on Wed Apr 17 16:09:46 2019

@author: madhu
"""
import urllib.request as ur
from urllib.parse import quote 
import json


title = input ('Type a movie Title:')
url = 'http://www.omdbapi.com/?apikey=FF68a35f&t=%s' % quote(title)
#url = 'http://www.omdbapi.com/?apikey=FF68a35f&t=eegah&y=1962'
try:

    print(url)
    conn = ur.urlopen(url)
    the_status = conn.status
    print('HTTP Status code:', the_status)
    if the_status in range(200,300):
        print(conn)
        data = conn.read()
        print('*'*30)
        print(data)
        print('*'*30)
        cont_type = conn.getheader('Content-Type')
        print(cont_type)
        print('*'*30)
        if 'json' in cont_type:
            str_data = data.decode('UTF-8')
            js_data = json.loads(str_data)
            print('*'*30)
            print(js_data)
            print('*'*30)
            print('Title :', js_data['Title'])
            print('*'*30)
            print('plot :', js_data['Plot'])
            print('*'*30)
            print('Headers:')
            for key, value in conn.getheaders():
                print(key, value)
            print('*'*30)
    
    
except:
    print('Sorry, Error accessing url', url)    