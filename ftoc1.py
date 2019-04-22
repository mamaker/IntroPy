# -*- coding: utf-8 -*-
"""
ftoc1.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


F_BOIL_TEMP = 212.0
F_FREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RANGE = F_BOIL_TEMP - F_FREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE / F_RANGE


def ftoc(f_temp):
    "Convert Fahrenheit temperature <f_temp> to Celsius and return it."
    c_temp = (f_temp - F_FREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_temp

#%%
if __name__ == '__main__':
    for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print('%8.3f F => %8.3f C' % (f_temp, c_temp))
    print('-'*30)
#%%
        
#%%
    for f_temp in [-40.0, -0.0, -32.0, -100.0, -212.0]:
        c_temp = ftoc(f_temp)
        print('%8.3f F => %8.3f C' % (f_temp, c_temp))
    print('-'*30)
#%%
    
#%%
    for f_temp in [40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print('%8.3f F => %8.3f C' % (f_temp, c_temp))
    print('-'*30)
#%%    