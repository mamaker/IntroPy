# -*- coding: utf-8 -*-
"""
pickling.py
Created on Sun Apr 14 20:31:57 2019

@author: madhu
"""
import pickle
import datetime

class Tiny():
    def __str__(self):
        return 'tiny'

try:
#%%    
    print('-'*20)
    now1 = datetime.datetime.utcnow()
    pickled = pickle.dumps(now1)
    print('now1:',now1)
    now2 = pickle.loads(pickled)
    print('now2:',now2)
    print('now1 = now2?',now1 == now2)
#%%
    
#%%   
    print('-'*20)
    obj1 = Tiny()
    print('obj1:', obj1)
    print('str(obj1):', str(obj1))
    pickled = pickle.dumps(obj1)
    print('obj1:',obj1)
    obj2 = pickle.loads(pickled)
    print('obj2:',obj2)
    print('obj1 = obj2?', str(obj1) == str(obj2))
#%%
    
except:
    print('Error Pickling!')
