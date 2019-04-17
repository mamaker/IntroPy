# -*- coding: utf-8 -*-
"""
redistst.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu
https://redislabs.com/community/ebook/
https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/
https://github.com/dmajkic/redis/downloads
C:\max\myApplix\Redis\64bit\redis-server 
"""
import redis

redisServer = 'localhost'
redisPort = 6379

try:
    conn = redis.Redis()
#    conn = redis.Redis(redisServer)
#    conn = redis.Redis(redisServer, redisPort)
    
    #%%
    print('All Keys: ', conn.keys('*'))
    
    if conn.set('secret', 'ni!'):
        print('secret = ', conn.get('secret'))
    
        
    #%%

    
except:
    print('Error accessing redis server {0} at port# {1}.'.format(redisServer, redisPort))
