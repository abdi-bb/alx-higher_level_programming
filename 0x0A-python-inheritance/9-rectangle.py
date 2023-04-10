#!/usr/bin/python3

'''
Module name: '9-rectangle'
Contained functions or subclass:
    subclass Rectangle
'''


class BaseGeometry:
    '''Represents BaseGeometry'''

    def integer_validator(self, name, value):
        '''Validates value'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    '''Represents Rectangle'''

    def __init__(self, width, height):
        '''Instantiates new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        '''returns area of Rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''returns [Rectangle] <width>/<height>'''
        return f'[Rectangle] {self.__width}/{self.__height}'
