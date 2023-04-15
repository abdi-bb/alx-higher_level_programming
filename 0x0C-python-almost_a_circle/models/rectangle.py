#!/usr/bin/python3

'''
Module name: 'rectangle'
Class names:
    Rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''Represent class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''instantiation of Rectangle'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self):
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self):
        self.__y = y
