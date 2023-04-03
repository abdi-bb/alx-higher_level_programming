#!/usr/bin/python3

'''Define a class Rectangle.'''


class Rectangle:
    '''Represent Rectangle.'''

    def __init__(self, width=0, height=0):
        '''Instantiation of the current rectangle.

        Args:
            width (int): width of the current rectangle
            height (int): height of the current rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets the width of the current rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the current height of the rectangle'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Get the current height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the current height of the rectangle.'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Returns the rectangle area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''Returns printable string representation of the rectangle.'''
        rectangle_list = ['']
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                [rectangle_list.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rectangle_list.append('\n')
        return ''.join(rectangle_list)

    def __repr__(self):
        '''Returns a string representation of the rectangle.'''
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
