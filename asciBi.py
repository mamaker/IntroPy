# -*- coding: utf-8 -*-
"""
asciBi.py
Created on Sat Apr 13 11:59:04 2019

@author: madhu
"""

import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
#b'89504e470d0a1a0a
print(binascii.unhexlify(b'89504e470d0a1a0a'))
#b'\x89PNG\r\n\x1a\n'
print(int('89504e470d0a1a0a',16))
#9894494448401390090

print('')
some_hex = b'\x9a'
print(binascii.hexlify(some_hex))
#b'9a
print(binascii.unhexlify(b'9a'))
#b'\x9a'
print(int('9a',16))
#154

print(b'a string','=', b'a string'.decode('ascii'))
