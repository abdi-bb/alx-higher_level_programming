#!/usr/bin/python3

'''
Module name: 'square'
Class:
    Square
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Instantiation of new square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns the described string format'''
        return '[{}] ({}) {}/{} - {}'.format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getter for size attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size attribute'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''That assigns multiple arguments to the attributes'''
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        '''Dictionary representation of a Square'''
        return {'id': getattr(self, "id"), 'size': getattr(
            self, "width"), 'x': getattr(self, "x"), 'y': getattr(self, "y")}
