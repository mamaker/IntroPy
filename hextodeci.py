# -*- coding: utf-8 -*-
"""
.py
Created on Sat Apr 13 09:07:57 2019

@author: madhu
"""

import struct
import binascii

valid_png_header = b'\x89PNG\r\n\x1a\n'
#OreillyLogo: http://bit.ly/orm-logo
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')
print('')
struct.pack('>L', 154)
struct.pack('>L', 141)

print('')
byt = bytes(b'\x9a') 
i = int('9a', 16)

print('')
print('convert this hex string to a bytes variable called gif.')
xstr =  '47494638396101000100800000000000ffffff21f9' + \
        '0401000000002c000000000100010000020144003b'
gif =  binascii.unhexlify(xstr)       
print(gif)  
print('Length: ',len(gif))
print('Is string a GIF?', gif[:6] == b'GIF89a')

print('')
print('The pixel width of a GIF is a 16-bit big-endian integer starting at byte offset 6, and' +\
'the height is the same size, starting at offset 8')        
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)