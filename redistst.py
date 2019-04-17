# -*- coding: utf-8 -*-
"""
redistst.py
Strings
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
    print('')
    print('check 1:')
    print('All Keys: ', conn.keys('*'))
    
    print('')
    print('check 2:')
    if conn.set('secret', 'ni!'):
        print('secret = ', conn.get('secret'), ' = ', conn.get('secret').decode('UTF-8'))
    
    print('')
    print('check 3:')
    if conn.set('carats', 24):
        print('carats = ', conn.get('carats'), ' = ', conn.get('carats').decode('UTF-8'))
    
    print('')
    print('check 4:')
    if conn.set('fever', 101.5):
        print('fever = ', conn.get('fever'), ' = ', conn.get('fever').decode('UTF-8'))
    
    print('')
    print('check 5:')
    if not conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!'):
        print('setnx() will not reset the value of "secret" since that key alredy exists.')
    if conn.set('secret', 'ni!'):
        print('secret = ', conn.get('secret'), ' = ', conn.get('secret').decode('UTF-8'))

    print('')
    print('check 6:')
    print('getset() method returns the old value and sets it to a new one at the same time:')
    prev_secret = conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')
    print('prev_secret = ', prev_secret.decode('UTF-8'))
    print('current secret = ', conn.get('secret'), ' = ', conn.get('secret').decode('UTF-8'))
    
    print('')
    print('check 7:')
    print('Get a substring by using getrange() (as in Python, offset 0=start, -1=end):')
    the_range = conn.getrange('secret', -6, -1)
    print('the_range = ', the_range, ' = ', the_range.decode('UTF-8'))

    print('')
    print('check 8:')
    print('Replace a substring by using setrange() (using a zero-based offset):')        
    string_len = conn.setrange('secret', 0, 'ICKY')
    print('string_len = ', string_len)
    print('current secret = ', conn.get('secret'), ' = ', conn.get('secret').decode('UTF-8'))

    print('')
    print('check 9:')
    if conn.mset({'pie': 'cherry', 'cordial': 'sherry'}):
        print('pie = ', conn.get('pie'), ' = ', conn.get('pie').decode('UTF-8'))
        print('cordial = ', conn.get('cordial'), ' = ', conn.get('cordial').decode('UTF-8'))

    print('')
    print('check 10:')
    mlist = conn.mget(['fever', 'carats'])
    for bstring in mlist:
        print('bstring', ' = ', bstring.decode('UTF-8'))
            
    print('')
    print('check 11:')
    if conn.delete('fever'):
        print('fever gone!')

    print('')
    print('check 12:')
    inc_carats = conn.incr('carats')
    print('incremented carats = ', inc_carats)
    inc_carats = conn.incr('carats', 10)
    print('incremented by 10 carats = ', inc_carats)

    print('')
    print('check 13:')
    dec_carats = conn.incr('carats')
    print('decremented carats = ', dec_carats)
    dec_carats = conn.incr('carats', 15)
    print('decremented by 15 carats = ', dec_carats)

    print('')
    print('check 14:')
    if conn.set('fever', 102.5):
        print('fever = ', conn.get('fever'), ' = ', conn.get('fever').decode('UTF-8'))
    inc_float = conn.incrbyfloat('fever')
    print('incremented float = ', inc_float)
    inc_float = conn.incrbyfloat('fever', 0.5)
    print('incremented by 0.5 float = ', inc_float)


    #%%

    
except:
    print('Error accessing redis server {0} at port# {1}.'.format(redisServer, redisPort))
