# -*- coding: utf-8 -*-
"""
writeBinary.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
"""

filename = 'bfile.bin'

writemode = 'w'
firstWritemode = 'x'
appendmode = 'a'

binaryfile = 'b'

modes = writemode+binaryfile
#modes = firstWritemode+binaryfile
#modes = appendmode+binaryfile

bdata = bytes(range(0, 256))
try:
    fout = open(filename, modes) # 'wb'

#%%
#    byts = fout.write(bdata)
#%%
    
    byts = 0
    size = len(bdata)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        byts += fout.write(bdata[offset:offset+chunk])
        offset += chunk

    fout.flush()
    fout.close()
    print('Wrote binary file %s, with %d bytes' % (filename, byts))

except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fout' in locals():
        fout.close()

