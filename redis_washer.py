# -*- coding: utf-8 -*-
"""
redis_washer.py
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
print('Washer is starting')
dishes = ['salad', 'bread', 'entree', 'dessert']
for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
conn.rpush('dishes', 'quit')
print('Washer is done')
    
