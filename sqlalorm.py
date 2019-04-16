# -*- coding: utf-8 -*-
"""
sqlalorm.py
Created on Tue Apr 16 12:01:01 2019

@author: madhu
"""
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#database = '/:memory:'
database = '/sqlalorm.db'


try:
    conn = sa.create_engine('sqlite://'+database)

#%%
    Base  = declarative_base()
    class Zoo(Base):
        __tablename__ = 'zoo'
        critter = sa.Column('critter', sa.String, primary_key = True)
        count = sa.Column('count', sa.Integer)
        damages = sa.Column('damages', sa.Float)
        def __init__(self, critter, count, damages):
            self.critter = critter
            self.count = count
            self.damages = damages
        def __repr__(self):
            return 'Zoo({},{},{})'.format(self.critter, self.count, self.damages)
    Base.metadata.create_all(conn)
#%%

#%%
    first = Zoo("duck", 10, 0.0)
    print(first)
    second = Zoo("bear", 2, 1000.0)
    print(second)
    third = Zoo('weasel', 1, 2000.0)
    print(third)

    Session = sessionmaker(bind=conn)
    session = Session()
    session.add(first)
    session.add_all([second, third])

    session.commit()    
#%%

except:
    print('Error accessing database {0}.'.format(database))
