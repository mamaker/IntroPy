# -*- coding: utf-8 -*-
"""
UnicNames.py
Created on Tue Apr  9 19:02:08 2019

@author: madhu
"""
import unicodedata
mystery = '\U0001f4a9'
print(mystery)

print('Name:')
mys_name = unicodedata.name(mystery)
print(mys_name)

print('Value:')
mys_val = unicodedata.lookup(mys_name)
print(mys_val)

print('UTF-8 Encoded:')
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

print('Decoded from UTF-8:')
pop_string = pop_bytes.decode('UTF-8')
print(pop_string)
print('Equal?',pop_string == mystery)



