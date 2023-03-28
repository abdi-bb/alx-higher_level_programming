#!/usr/bin/python3

'''Define a class Square.'''


class Square:
    '''Represents the new square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new square.

        Args:
            size (int): The size of new square.
            position (unsigned int, unsigned int): The position of the square.
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Get the current size of the square.'''
        return (self.__size)

    @property
    def position(self):
        '''Gets the current position of the square.'''
        return (self.__position)

    @size.setter
    def size(self, value):
        '''Get/set the current size of the square.'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        '''Set the current position of the square.'''
        if not isinstance(value, tuple(int, int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''Return the current area of the square.'''
        return (self.__size**2)

    def my_print(self):
        '''Print the square with the # character.'''
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
