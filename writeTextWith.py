# -*- coding: utf-8 -*-
"""
writeTextWith.py
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
modes = firstWritemode+textfile
#modes = appendmode+textfile

try:
    with open(filename, modes) as fout:
        byts = fout.write(poem)
        fout.flush()
    
    print('Wrote text file %s, with %d bytes' % (filename, byts))
    
except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fout' in locals():
        fout.close()


