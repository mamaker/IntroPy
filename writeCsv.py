# -*- coding: utf-8 -*-
"""
writeCsv.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
"""
import csv

villains =  [['FIRST NAME', 'LAST NAME'], # Header (Column Names)
            ['Doctor', 'No'],
            ['Rosa', 'Klebb'],
            ['Mister', 'Big'],
            ['Auric', 'Goldfinger'],
            ['Ernst', 'Blofeld'],
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
    rows = len(villains)
    with open(filename, modes, newline='') as fout:
        csvout = csv.writer(fout)
#%%
        csvout.writerows(villains)
#%%

#%%
#        for row in villains:
#            csvout.writerow(row)
#%%    
    print('Wrote csv file %s, with %d rows' % (filename, rows))
    
except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fout' in locals():
        fout.close()


