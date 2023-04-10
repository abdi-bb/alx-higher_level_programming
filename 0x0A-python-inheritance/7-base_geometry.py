#!/usr/bin/python3

'''
Module name: '7-base_geometry'
Contained functions:
    base_geometry
'''


class BaseGeometry:
    '''Represents BaseGeometry'''

    def area(self):
        '''Raises Exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
