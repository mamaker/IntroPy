# -*- coding: utf-8 -*-
"""
dump_test.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""

def func(*args, **kwargs):
    print(vars())


#%%
print("Calling func: func(1, 2, 3):")
func(1, 2, 3)
print('-'*30)
#%%

#%%
print("Calling func: func(['a', 'b', 'argh']):")
func(['a', 'b', 'argh'])
print('-'*30)
#%%

#%%
print("Calling func: func(1, 'a',[2, 'b', 'argh'], boy='John', girl='Jane'):")
func(1, 'a',[2, 'b', 'argh'], boy='Jojn', girl='Jane')
print('-'*30)
#%%

