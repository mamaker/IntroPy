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

days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

#%%
print('')
print('check 1:')
print('All Keys: ', conn.keys('*'))

print('')
print('check 2:')
onSide = conn.setbit(days[0], big_spender, 1)
print('Set bit for days[0],big_spender:', onSide)

conn.setbit(days[0], tire_kicker, 1)
conn.setbit(days[1], big_spender, 1)
conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)

#print('')
#print('check 3:')
#print('bitcounts for the days:')
#for day in days:
#    conn.bitcount(tire_kicker)
#    pass

print('')
print('check 4:')
the_bits = conn.getbit(days[1], tire_kicker)
print('Did user tire_kicker visit on day 2?: ', the_bits) 

#print('')
#print('check 5:')
#conn.bitop('and', 'everyday', *days)
#print('How many users visited every day?: ', conn.bitcount('everyday')) 
#
#print('')
#print('check 6:')
#if conn.getbit('everyday', big_spender):
#    print('Yes, it was big_spender!')
#%%

#%%
key = 'now you see it'
if conn.set(key, 'but not for long'):
    if conn.expire(key, 5):
        conn.ttl(key)
        print('key available?',conn.get(key))
        time.sleep(6)
        print('key available?',conn.get(key))
#%%

    
