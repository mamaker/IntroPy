# -*- coding: utf-8 -*-
"""
sqlaltst.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu
"""
import sqlalchemy as sa

#database = '/:memory:'
database = '/sqlalite.db'


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

def exec_qry(conn, cols, qry_str):
    rows = conn.execute(qry_str)
    show_tbl(rows, cols)
    return

try:
    conn = sa.create_engine('sqlite://'+database)

#%%
    conn.execute('''CREATE TABLE zoo
                 (critter VARCHAR(20) PRIMARY KEY,
                 count INT,
                 damages FLOAT
                 )
                 ''')
#%%
    columns = ['critter','count','damages']   
    cols = ','.join(columns)

#%%
    ins = 'INSERT INTO zoo ('+cols+') VALUES(?,?,?)'
    conn.execute(ins, "duck", 10, 0.0) 
    conn.execute(ins, "bear", 2, 1000.0) 
    conn.execute(ins, 'weasel', 1, 2000.0) 
#%%

#%%
    qry_str = 'SELECT * from zoo'
    exec_qry(conn, columns, qry_str)
    qry_str = 'SELECT * from zoo ORDER BY count'
    exec_qry(conn, columns, qry_str)

    qry_str = 'SELECT * from zoo ORDER BY count DESC'
    exec_qry(conn, columns, qry_str)
    
    qry_str = '''
                SELECT * from zoo WHERE
                damages = (SELECT MAX(damages) from zoo)
    '''
    exec_qry(conn, columns, qry_str)
#%%        

except:
    print('Error accessing database {0}.'.format(database))
