# -*- coding: utf-8 -*-
"""
redistst5.py
Sorted Sets
Created on Tue Apr 16 12:01:01 2019

@author: madhu
https://redislabs.com/community/ebook/
https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/
https://github.com/dmajkic/redis/downloads
C:\max\myApplix\Redis\64bit\redis-server 
"""
import redis
import time

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
now = time.time()
print('Current time:', now)

#print('')
#print('check 3:')
#num_added = conn.zadd('logins', 25, 'smeagol')
#print('num_added: ', num_added)

print('')
print('check 4:')
ordered_list = conn.zrange('logins', 0, -1)
print('ordered list: ', ordered_list)

#print('')
#print('check 5:')
#conn.zadd('logins', 'sauron', now+(5*60))
#print('num_added: ', num_added)




#%%

    
