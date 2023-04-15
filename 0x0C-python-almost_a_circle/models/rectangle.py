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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''returns the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Returns the height attr'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height attribute'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        '''gets the attribute x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        '''grabs y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        '''returns area value of rectangle instance'''
        return self.__width * self.__height
