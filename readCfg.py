# -*- coding: utf-8 -*-
"""
readCfg.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
settings.cfg:
[english]
greeting = Hello

[french]
greeting = Bonjour

[files]
home = /usr/local
# simple interpolation:
bin = %(home)s/bin
"""
import configparser
filename = 'settings.cfg'
try:
    cfg = configparser.ConfigParser()
    cfg.read(filename)
    
    print('french:', cfg['french'])
    print('french, greeting:', cfg['french']['greeting'])
    print('files, bin:', cfg['files']['bin'])   

except:
    print('Error accessing file %s ' % filename)
    

