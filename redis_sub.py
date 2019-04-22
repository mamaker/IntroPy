# -*- coding: utf-8 -*-
"""
redis_sub.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
https://redislabs.com/community/ebook/
https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/
https://github.com/dmajkic/redis/downloads

C:\max\myApplix\Redis\64bit>redis-server
python redis_sub.py
python redis_pub.py
"""
import redis

conn = redis.Redis()
topics = ['maine coon', 'persian']
sub = conn.pubsub()
sub.subscribe(topics)
print('Subscriber: Ready and listening, waiting...')
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: %s wears a %s' % (cat, hat))