# -*- coding: utf-8 -*-
"""
dates1.py
Created on Thu Apr 18 17:28:37 2019

@author: madhu
"""
fmt_local = "\nIt's %A, %B %d, %Y, local time %I:%M:%S%p"
fmt_UTC = "\nIt's %A, %B %d, %Y, UTC time %I:%M:%S%p"

#%%
from datetime import date
print('-'*30)
halloween = date(2014, 10, 31)
print('halloween:',halloween)
print('halloween.day:',halloween.day)
print('halloween.month:',halloween.month)
print('halloween.year:',halloween.year)
#%%

#%%
from datetime import date
print('-'*30)
this_day = date.today()
print('this_day:',this_day, this_day.strftime(fmt_local))
print('this_day.day:',this_day.day)
print('this_day.month:',this_day.month)
print('this_day.year:',this_day.year)

#%%

#%%
from datetime import timedelta
print('-'*30)
one_day = timedelta(days=1)
tomorrow = this_day + one_day
print('tomorrow:',tomorrow)
#%%

#%%
print('-'*30)
days_ahead = 17
future_day = this_day + (one_day * days_ahead)
print(days_ahead, 'days_ahead:',future_day)
#%%

#%%
print('-'*30)
days_ago = 10
past_day = this_day - (one_day * days_ago)
print(days_ago, 'days_ago:',past_day)

#%%
from datetime import time
print('-'*30)
noon = time(12,30,15)
print('noon:',noon, noon.strftime(fmt_local))
print('noon.hour:', noon.hour)
print('noon.minute:', noon.minute)
print('noon.second:', noon.second)

#%%

#%%
from datetime import datetime
print('-'*30)
right_now = datetime.now()
print('right_now:',right_now)
print('right_now.isoformat:',right_now.isoformat())
print('right_now.day:',right_now.day)
print('right_now.month:',right_now.month)
print('right_now.year:',right_now.year)
print('right_now.hour:', right_now.hour)
print('right_now.minute:', right_now.minute)
print('right_now.second:', right_now.second)
print('right_now.microsecond:', right_now.microsecond)

#%%

#%%
from datetime import datetime
print('-'*30)
print('this_day:',type(this_day), this_day)
print('noon:',type(noon),noon)
noon_today = datetime.combine(this_day, noon)
print('noon_today:',type(noon_today),noon_today)
today_date = noon_today.date()
print('today_date:',type(today_date), today_date)
today_noon = noon_today.time()
print('today_noon:',type(today_noon), today_noon)

#%%

#%%
import time
print('-'*30)
epoch_now = time.time()
print('epoch_now:',type(epoch_now), epoch_now)
time_now = time.ctime(epoch_now)
print('time_now:',type(time_now), time_now)
print('-'*30)
local_time = time.localtime()
print('local_time:',type(local_time), time.strftime(fmt_local,local_time))
print('-'*30)
utc_time = time.gmtime(epoch_now)
print('utc_time:',type(utc_time), time.strftime(fmt_UTC, utc_time))
print('-'*30)
time_fmt = '%Y-%m-%d'
date_time = time.strptime('2019-01-29', time_fmt)
print('date_time:',date_time, time.strftime(fmt_local, date_time))

#%%



