# -*- coding: utf-8 -*-
"""
redis_dryer.py
Lists
Created on Tue Apr 16 12:01:01 2019

@author: madhu
https://redislabs.com/community/ebook/
https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/
https://github.com/dmajkic/redis/downloads

C:\max\myApplix\Redis\64bit>redis-server
C:\max\PyStuf\IntroPy>start /b python redis_dryer.py 
C:\max\PyStuf\IntroPy>python redis_washer.py 
"""
import redis

conn = redis.Redis()
print('Dryer is starting')
while True:
    msg = conn.blpop('dishes')
    if not msg:
        break
    val = msg[1].decode('utf-8')
    if val == 'quit':
        break
    print('Dried', val)
print('Dishes are dried')

