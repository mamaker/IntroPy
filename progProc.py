# -*- coding: utf-8 -*-
"""
progProc.py
Created on Thu Apr 18 17:28:37 2019

@author: madhu
"""
import os
import subprocess

try:
   
#%%
    print('-'*30)
    i = 0
    process_id = os.getpid()
    print('\t'*i,'process_id:', process_id); i += 1
#    user_id = os.getuid()
#    print('\t'*i,'user_id:', user_id); i += 1
#    group_id = os.getgid()
#    print('\t'*i,'group_id:', group_id); i += 1
    
#%%
    print('-'*30)
    retval = subprocess.getoutput('dir')
    print('dir:', retval)
    print('-'*30)
    retval = subprocess.getoutput('dir /w')
    print('dir /w:', retval)
#    print('-'*30)
#    retval = subprocess.check_output(['dir', 'echo'])
#    print('\t'*i,'date:', retval); i += 1
    print('-'*30)
    retval = subprocess.getstatusoutput('dir /w')
    print('(status, date):', retval)
    print('-'*30)
    retval = subprocess.call('python pickling.py')
    print('status of running <python pickling.py>:', retval)

#%%

#%%



except:
    print('Sorry, error in program process')