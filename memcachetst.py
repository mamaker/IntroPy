# -*- coding: utf-8 -*-
"""
memcachetst.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu

C:\max\myApplix\memcached>memcached.exe -d start 
C:\max\myApplix\memcached>memcached.exe -d stop
C:\max\myApplix\memcached>memcached.exe -help
"""
import memcache

memServer = ['127.0.0.1:11211']

try:
    db = memcache.Client(['127.0.0.1:11211'])
    
    #%%
    
    if db.set('marco', 'polo'):
        print('marco = ',db.get('marco'))
    
    if db.set('ducks', 0):
        print('ducks = ',db.get('ducks'))
    
    if db.incr('ducks', 2):
        print('ducks Incremented by 2 = ',db.get('ducks'))
    
        
    #%%

except:
    print('Error accessing memcache server {0}.'.format(memServer))
