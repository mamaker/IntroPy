# -*- coding: utf-8 -*-
"""
readCsv.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
"""
import csv

filename = 'villains.csv'

readmode = 'r'

textfile = 't'

modes = readmode+textfile

villains =  []
try:
    with open(filename, modes, newline='') as fin:
        csvin = csv.reader(fin)

#%%
#        villains = [row for row in csvin]
#%%
        
#%%        
        next(csvin)    # skip Header (Column Names)
        for row in csvin:
            villains.append(row) 
#%%
    rows = len(villains)
    print('Read in %d rows of csv file %s.' % (rows, filename))
    print(villains)    
except:
    print('Error accessing file %s in %s mode!' % (filename, modes))
    if 'fout' in locals():
        fin.close()


