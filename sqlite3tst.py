# -*- coding: utf-8 -*-
"""
sqlite3tst.py

Created on Tue Apr 16 10:04:08 2019

@author: madhu
"""
import sqlite3
database = 'sqllttst.db'

def show_hdr(cols, colfactor):
    print('')
    print('-'*(colfactor*(len(cols)-1)))
    for col in cols:
        print('%-20s' % col, end='')
    print('-'*(colfactor*(len(cols)-1)))
    return


def show_tbl(rows, cols):
    colfactor = 20+5 
    show_hdr(cols, colfactor)
    for row in rows:
        for i in range(len(row)):
            print('%-20s' % row[i], end='')
    print('')
    return

def exec_qry(curs, cols, qry_str):
    curs.execute(qry_str)
    rows = curs.fetchall()
    show_tbl(rows, cols)
    return

try:
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    
    #%%
#    curs.execute('''CREATE TABLE zoo
#                 (critter VARCHAR(20) PRIMARY KEY,
#                 count INT,
#                 damages FLOAT
#                 )
#                 ''')
    #%%

    columns = ['critter','count','damages']   
    cols = ','.join(columns)

    #%%
#    curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)') 
#    curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)') 
#    ins = 'INSERT INTO zoo ('+cols+') VALUES(?,?,?)'
#    curs.execute(ins, ('weasel', 1, 2000.0))   # prevent SQL Injection
#    conn.commit()
    #%%
        
    #%%
    qry_str = 'SELECT * from zoo'
    exec_qry(curs, columns, qry_str)

    qry_str = 'SELECT * from zoo ORDER BY count'
    exec_qry(curs, columns, qry_str)

    qry_str = 'SELECT * from zoo ORDER BY count DESC'
    exec_qry(curs, columns, qry_str)
    
    qry_str = '''
                SELECT * from zoo WHERE
                damages = (SELECT MAX(damages) from zoo)
    '''
    exec_qry(curs, columns, qry_str)

    #%%

    curs.close()
    conn.close()

except:
    if 'curs' in locals():
        curs.close()
    if 'conn' in locals():
        conn.close()
    print('Error accessing database {0}.'.format(database))

