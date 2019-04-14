# -*- coding: utf-8 -*-
"""
seekBinary.py
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

    print(' ')
    byt_pos = fin.tell()
    print('In BOF binary file %s, current read position is: %d.' % (filename,byt_pos))
    print('Going to One byte before the end of the file:')
    byt_pos = fin.seek(255)
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))
    bdata = fin.read()
    byts = len(bdata)
    print('Finished reading in last %d bytes of binary file %s' % (byts, filename))
    byt_pos = fin.tell()
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))

    print(' ')
    byt_pos = fin.seek(0)
    print('In BOF binary file %s, current read position is: %d.' % (filename,byt_pos))
    print('Going to One byte before the end of the file:')
    byt_pos = fin.seek(-1, 2)
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))
    print('In binary file %s, current read position per tell(): %d.' % (filename,fin.tell()))
    bdata = fin.read()
    byts = len(bdata)
    print('Finished reading in last %d bytes of binary file %s' % (byts, filename))
    byt_pos = fin.tell()
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))

#   seek(offset, origin)
#If origin is 0 (the default), go offset bytes from the start
#If origin is 1 , go offset bytes from the current position
#If origin is 2 , go offset bytes relative to the end
    print(' ')
    byt_pos = fin.seek(0)
    print('In BOF binary file %s, current read position is: %d.' % (filename,byt_pos))
    print('Going to Two bytes before the end of the file:')
    byt_pos = fin.seek(-2, 2)
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))
    print('In binary file %s, current read position per tell(): %d.' % (filename,fin.tell()))
    print('Going forward One byte:')
    byt_pos = fin.seek(1, 1)
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))
    print('In binary file %s, current read position per tell(): %d.' % (filename,fin.tell()))
    bdata = fin.read()
    byts = len(bdata)
    print('Finished reading in last %d bytes of binary file %s' % (byts, filename))
    byt_pos = fin.tell()
    print('In binary file %s, current read position is: %d.' % (filename,byt_pos))

    fin.close()

except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fin' in locals():
        fin.close()

