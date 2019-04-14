# -*- coding: utf-8 -*-
"""
readBinary.py
Created on Sat Apr 13 19:40:00 2019

@author: madhu
"""

filename = 'bfile.bin'

readmode = 'r'

binaryfile = 'b'

modes = readmode+binaryfile

poem = ''
try:
    fin = open(filename, modes) # 'rb'

#%%
    bdata = fin.read()
#%%
    
    fin.close()

    byts = len(bdata)
    print('Read in %d bytes of binary file %s' % (byts, filename))

except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fin' in locals():
        fin.close()

