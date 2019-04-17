# -*- coding: utf-8 -*-
"""
dbmread.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu
"""
import dbm

database = 'dbmtest'
mode = 'c' 

try:
    db = dbm.open(database, mode)

#%%
    
    print('Number of items defined :', len(db))
    print(db['ketchup'], '=', db['ketchup'].decode('ascii'))
    print('pesto = ',db.get('pesto'))
    print('mustard = ', db.setdefault('mustard', 'some color'))
#    print('berry = ', db.setdefault('berry', 'some color'))
    print('All defined keys:')
    for key in db:  
        print(key)
    
#%%

    db.close()

except:
    print('Error accessing database {0}.'.format(database))
