# -*- coding: utf-8 -*-
"""
redistst3.py
Hash
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


conn = redis.Redis()
#    conn = redis.Redis(redisServer)
#    conn = redis.Redis(redisServer, redisPort)

#%%
print('')
print('check 1:')
print('All Keys: ', conn.keys('*'))

print('')
print('check 2:')
if conn.hmset('song', {'do': 'a deer', 're': 'about a deer'}):
    print('song:', conn.hlen('song'), conn.hgetall('song'))
    print('song keys:',conn.hkeys('song'))
    print('song values:',conn.hvals('song'))

print('')
print('check 3:')
num_of_field_set = conn.hset('song', 'mi', 'a note to follow re') # single 
print('num_of_field_set:', num_of_field_set)

print('')
print('check 4:')
print('just mi:',conn.hget('song', 'mi'))

print('')
print('check 5:')
print('getting multiple values:', conn.hmget('song', 're', 'do'))

#%%

    
