# -*- coding: utf-8 -*-
"""
jsonStr.py
Created on Sun Apr 14 14:36:41 2019

@author: madhu
"""
import json
import datetime
from time import mktime

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

#%%
menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
                    }
            },
        "lunch" : {
            "hours": "11-3",
            "items": {
                    "hamburger": "$5.00"
                    }
            },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }
            
menu_json = json.dumps(menu)   
print('Jason string:\n'+menu_json)  

print('')
menu2 = json.loads(menu_json)   
print('menu Dictionary:\n',menu2) 

print('')
print('menu = menu2?', menu == menu2)
#%%

print('')
now = datetime.datetime.utcnow()
print('Datetime now:', now)
#%%
now_json = json.dumps(str(now))
print('Json now string:', now_json)
#%%

#%%
print('')
now_epoch = int(mktime(now.timetuple()))
print('now_epoch:', now_epoch)
json_now_epoch = json.dumps(now_epoch)
print('Json now_epoch:', json_now_epoch)
#%%

#%%
print('')
json_DTEncoder_str = json.dumps(now, cls=DTEncoder)
print('json_DTEncoder:', json_DTEncoder_str)

#%%





 
            