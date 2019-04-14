# -*- coding: utf-8 -*-
"""
readText.py
Created on Sat Apr 13 19:40:00 2019

@author: madhu
"""

filename = 'relativity.txt'

readmode = 'r'

textfile = 't'

modes = readmode+textfile

poem = ''
try:
    fin = open(filename, modes) # 'rt'

#%%
#    poem = fin.read()
#%%
    
#%%
#    for line in fin:
#        poem += line
#%%
    
#%%    
#    chunk = 100
#    while True:
#        fragment = fin.read(chunk)
#        if not fragment:
#            break
#        poem += fragment
#%%
    
#%%    
#    while True:
#        line = fin.readline()
#        if not line:
#            break;
#        poem += line
#%%
    
#%%    
    lines = fin.readlines()
    n = 0
    for line in lines:
        poem += line
        n += 1
    print('%d lines read' % n)    
#%%    


    fin.close()

    byts = len(poem)
    print('Read in %d bytes of text file %s' % (byts, filename))

except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fin' in locals():
        fin.close()

