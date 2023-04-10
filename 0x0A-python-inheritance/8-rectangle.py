#!/usr/bin/python3

'''
Module name: '8-rectangle'
Contained functions or subclass:
    subclass Rectangle
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents Rectangle'''

    def __init__(self, width, height):
        '''Instantiates new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
