# -*- coding: utf-8 -*-
"""
sqlalexp.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu
"""
import sqlalchemy as sa

#database = '/:memory:'
database = '/sqlalexp.db'


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

def exec_qry(conn, cols, qry):
    result = conn.execute(qry)
    rows = result.fetchall()
    show_tbl(rows, columns)
    return


try:
    conn = sa.create_engine('sqlite://'+database)
    meta = sa.MetaData()

#%%
    zoo = sa.Table('zoo', meta,
                 sa.Column('critter', sa.String, primary_key = True),
                 sa.Column('count', sa.Integer),
                 sa.Column('damages', sa.Float)
                 )
#    meta.create_all(conn)
#%%
    columns = ['critter','count','damages']   
    cols = ','.join(columns)

#%%
#    conn.execute(zoo.insert(("bear", 2, 1000.0)))
#    conn.execute(zoo.insert(('weasel', 1, 2000.0)))
#    conn.execute(zoo.insert(("duck", 10, 0.0))) 
#%%

#%%
#    SELECT * from zoo
#    result = conn.execute(zoo.select())
    qry = sa.select([zoo])
    exec_qry(conn, columns, qry)
#%%
  
#%%    
#    SELECT * from zoo ORDER BY count
    qry = sa.select([zoo]).order_by(zoo.columns.count)
    exec_qry(conn, columns, qry)
#%%
    
#%%    
#    SELECT * from zoo ORDER BY count DESC
    qry = sa.select([zoo]).order_by(sa.desc(zoo.columns.count))
    exec_qry(conn, columns, qry)
#%%
    
#%%    
#    SELECT * from zoo WHERE damages = (SELECT MAX(damages) from zoo)
    qry = sa.select([zoo]).where(zoo.columns.count == 10)
    exec_qry(conn, columns, qry)
#%%


except:
    print('Error accessing database {0}.'.format(database))
