#!/usr/bin/python3
'''
module: 'model_city'
Class: City
'''

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''Represents class City

    Attributes:
        __tablename__ (str): The name of the table of of class City
        id (int): The city id of the class City
        name (str): The city name of the class
    '''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
