# -*- coding: utf-8 -*-
"""
redistst2.py
Lists
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
pushed = conn.lpush('zoo', 'bear')
print('values in list: ', pushed)
print('Get a range of list values (use 0 to -1 for all)')
print(conn.lrange('zoo', 0, -1))

print('')
print('check 3:')
pushed = conn.rpush('zoo', 'yak')
print('values in list: ', pushed)
print('Get a range of list values (use 0 to -1 for all)')
print(conn.lrange('zoo', 0, -1))

#print('')
#print('check 4:')
#pushed = conn.lpush('zoo', 'alligator', 'duck')
#print('Keys pushed: ', pushed)

print('')
print('check 5:')
pushed = conn.linsert('zoo', 'before', 'bear', 'beaver')
print('values in list: ', pushed, conn.lrange('zoo', 0, -1))

print('')
print('check 6:')
pushed = conn.linsert('zoo', 'after', 'bear', 'cassowary')
print('values in list: ', pushed, conn.lrange('zoo', 0, -1))

print('')
print('check 7:')
pushed = conn.linsert('zoo', 'after', 'bear', 'cassowary')
print('values in list: ', pushed, conn.lrange('zoo', 0, -1))

print('')
print('check 8:')
if conn.lset('zoo', 2, 'marmoset'):
    print('values in list: ', conn.lrange('zoo', 0, -1))

print('')
print('check 9:')
the_value = conn.lindex('zoo', 3)
print('the_value: ', the_value, ' = ', the_value.decode('UTF-8'))

print('')
print('check 10:')
the_values = conn.lrange('zoo', 0, 2)
print('the_values: ', the_values)

print('')
print('check 11:')
if conn.ltrim('zoo', 1, 4):
   print('values in list: ', conn.lrange('zoo', 0, -1)) 



    #%%

    
