#!/usr/bin/python3

'''
Module name: '11-square'
Contained functions or subclass:
    subclass Rectangle
    subclass Square
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represen a Square'''

    def __init__(self, size):
        '''instantiates a square'''
        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        '''returns area of a square'''
        return self.__size**2

    def __str__(self):
        '''returns the required string description'''
        return f'[Square] {self.__size}/{self.__size}'
