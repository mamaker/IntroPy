# -*- coding: utf-8 -*-
"""
dates2.py
Created on Fri Apr 19 20:50:48 2019

@author: madhu
"""

#%%
import locale
from datetime import date
print('-'*30)
locale_keys = locale.locale_alias.keys()
good_keys = [key for key in locale_keys if len(key) == 5 and key[2] == '_']
halloween = date(2014, 10, 31)
#for each_local in good_keys:
#    print(each_local[0:2]+'-'+each_local[3:5])
#    good_key = each_local.replace('_', '-')
#    locale.setlocale(locale.LC_TIME,good_key)
#    print(halloween.strftime('%A, %B %d'))
print('-'*30)
for lang_country in ['fr-fr', 'de-de', 'es-es', 'is-is','en-US',]:
    locale.setlocale(locale.LC_TIME,lang_country)
    print(halloween.strftime('%A, %B %d'))
#%%
