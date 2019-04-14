# -*- coding: utf-8 -*-
"""
writeText.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
"""

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

filename = 'relativity.txt'

writemode = 'w'
firstWritemode = 'x'
appendmode = 'a'

textfile = 't'

#modes = writemode+textfile
#modes = firstWritemode+textfile
modes = appendmode+textfile

try:
    fout = open(filename, modes) # 'wt'
    byts = len(poem)

#%%
#    print('Wrote text file %s, with %d bytes' % (filename, byts))
#%%
    
#%%    
#    byts = fout.write(poem)
#    print('Wrote text file %s, with %d bytes' % (filename, byts))
#%%
    
#%%    
    offset = 0
    chunk = 100
    while True:
        if offset > byts:
            break
        fout.write(poem[offset:offset+chunk])
        offset += chunk
#%%
        
    fout.flush()
    fout.close()
    print('Wrote text file %s, with %d bytes' % (filename, byts))

except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fout' in locals():
        fout.close()

