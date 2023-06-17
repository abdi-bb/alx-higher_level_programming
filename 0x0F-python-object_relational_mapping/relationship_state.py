#!/usr/bin/python3

'''
module: 'relationship_state'
    Class definition of a class State
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

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
    cities = relationship('City', cascade='all, delete', back_populates='state')
