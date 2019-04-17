# -*- coding: utf-8 -*-
"""
dbmwrite.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu
"""
import dbm

database = 'dbmtest'
mode = 'c' 

try:
    db = dbm.open(database, mode)

#%%
    db['mustard'] = 'yellow'
    db['ketchup'] = 'red'
    db['pesto'] = 'green'
    
    print('Number of items defined :', len(db))
    print(db['ketchup'], '=', db['ketchup'].decode('ascii'))
    
#%%

    db.close()

except:
    print('Error accessing database {0}.'.format(database))
