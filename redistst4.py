# -*- coding: utf-8 -*-
"""
redistst4.py
Sets
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
how_many = conn.sadd('zoo2', 'duck', 'goat', 'turkey')
print('Add one or more (',how_many,') values to a set.')

print('')
print('check 3:')
how_many = conn.scard('zoo2')
print('The number of values from the set:',how_many)

print('')
print('check 4:')
print("Get all the set’s values:")
the_set = conn.smembers('zoo2')
print('The set:',the_set)

print('')
print('check 5:')
if conn.srem('zoo2', 'turkey'):
    the_set = conn.smembers('zoo2')
    print('The reduced set:',the_set)

print('')
print('check 6:')
how_many = conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')
print('Add one or more (',how_many,') values to a set.')

print('')
print('check 7:')
print('Get the common members of the zoo and better_zoo sets:')
the_set = conn.sinter('zoo2', 'better_zoo')
print('The common set:',the_set)

print('')
print('check 8:')
print('Get the intersection of zoo and better_zoo')
how_many = conn.sinterstore('fowl_zoo', 'zoo2', 'better_zoo')
print(how_many, 'member(s) in the intersection set:')
the_set = conn.smembers('fowl_zoo')
print('The intersection set:',the_set)

print('')
print('check 9:')
print('Get the union (all members) of zoo and better_zoo ')
the_set = conn.sunion('zoo2', 'better_zoo')
print('The union set:',the_set)

print('')
print('check 10:')
print('Store that union result in the set fabulous_zoo')
how_many = conn.sunionstore('fabulous_zoo', 'zoo2', 'better_zoo')
print(how_many, 'member(s) in the union set:')
the_set = conn.smembers('fabulous_zoo')
print('The union set:',the_set)

print('')
print('check 11:')
print('Get the set difference between zoo and better_zoo ')
the_set = conn.sdiff('zoo2', 'better_zoo')
print('The difference set:',the_set)

print('')
print('check 12:')
print('Store that difference result in the set zoo_sale')
how_many = conn.sdiffstore('zoo_sale', 'zoo2', 'better_zoo')
print(how_many, 'member(s) in the difference set:')
the_set = conn.smembers('zoo_sale')
print('The difference set:',the_set)


#%%

    
