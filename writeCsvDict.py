# -*- coding: utf-8 -*-
"""
writeCsv.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
"""
import csv

villains =  [
        {'FIRST NAME': 'Doctor','LAST NAME': 'No'},
        {'FIRST NAME': 'Rosa',  'LAST NAME': 'Klebb'},
        {'FIRST NAME': 'Mister','LAST NAME': 'Big'},
        {'FIRST NAME': 'Auric', 'LAST NAME': 'Goldfinger'},
        {'FIRST NAME': 'Ernst', 'LAST NAME': 'Blofeld'},
            ]

filename = 'villains.csv'

writemode = 'w'
firstWritemode = 'x'
appendmode = 'a'

textfile = 't'

modes = writemode+textfile
#modes = firstWritemode+textfile
#modes = appendmode+textfile

try:
    rows = len(villains) + 1 # including Header
    with open(filename, modes, newline='') as fout:
        fldnams = ['FIRST NAME', 'LAST NAME']
        csvout = csv.DictWriter(fout, fldnams)
        csvout.writeheader()
#%%
#        csvout.writerows(villains)
#%%

#%%
        for di in villains:
            csvout.writerow(di)
#%%    
    print('Wrote csv file %s, with %d rows' % (filename, rows))
    
except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fout' in locals():
        fout.close()


