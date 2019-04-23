# -*- coding: utf-8 -*-
"""
imghdr_test.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


import imghdr

file_name = 'oreilly.png'

print('File', file_name,'is a:', imghdr.what(file_name))
