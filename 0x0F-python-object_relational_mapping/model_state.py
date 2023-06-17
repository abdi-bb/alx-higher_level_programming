#!/usr/bin/python3

'''
module: 'model_state'
    Class definition of a class State and clase Base
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Represents class State
    Attributes:
        __tablename__ (str): table name of the class
        id (int): state id
        name (str): state name
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
