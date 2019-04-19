# -*- coding: utf-8 -*-
"""
leapYear.py
Created on Thu Apr 18 17:28:37 2019

@author: madhu
"""
import calendar

#%%

print('-'*30)
i = 0
isornot = {True: 'is', False: 'aint'}
year = 1900; print(year,'%s leap' % isornot.get(calendar.isleap(year)))
year = 1996; print(year,'%s leap' % isornot.get(calendar.isleap(year)))
year = 1999; print(year,'%s leap' % isornot.get(calendar.isleap(year)))
year = 2000; print(year,'%s leap' % isornot.get(calendar.isleap(year)))
year = 2002; print(year,'%s leap' % isornot.get(calendar.isleap(year)))
year = 2004; print(year,'%s leap' % isornot.get(calendar.isleap(year)))

#%%

