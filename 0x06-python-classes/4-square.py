#!/usr/bin/python3

'''Define class Square.'''


class Square:
    '''Represent a square'''

    def __init__(self, size=0) -> None:
        '''Initializing a new size.

        Args:
            size (int): size of the square.
        '''
        self.__size = size

    @property
    def size(self):
        '''Get the current size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setting the current size of the square.'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''Returns the current area of the Square.'''
        return (self.__size**2)
