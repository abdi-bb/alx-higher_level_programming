#!/usr/bin/python3

'''
Module name: '11-square'
Contained functions and subclasses:
    subclass Rectangle
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represents class Square'''

    def __init__(self, size):
        '''instantiates new square'''
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        return f'[Square] {size}/{size}'

    def area(self):
        '''returns area of square'''
        return self.__size**2
