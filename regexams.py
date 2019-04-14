# -*- coding: utf-8 -*-
"""
regexams.py
Created on Sat Apr 13 12:37:50 2019

@author: madhu
"""
import re

def showFinds(mats):
    print('location: ')    
    for m in mats:
        print(m.start(), end=',')
        print('\t', m.end(), end=',')
        print('\t', m.group())

    return

mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon
'''
print('')
print("All the words that begin with 'c'")
pat = r'\bc\w*'
finds = re.findall(pat, mammoth)
for cword in finds:
    print(cword)
print('')

print("All four-letter words that begin with 'c'")
pat = r'\bc\w{3}\b'
showFinds(re.finditer(pat, mammoth))
print('')

print("All the words that end with 'r'") 
pat = r"\b\w*r\b"
showFinds(re.finditer(pat, mammoth))
print('')

print("All the words that end with 'l'") 
pat = r"\b[\w']*l\b"
showFinds(re.finditer(pat, mammoth))
print('')

print("All the words that contain exactly three vowels in a row") 
pat = r"\b\w*[aeiou]{3}\w*\b"
showFinds(re.finditer(pat, mammoth))
print('')

print('Done')









