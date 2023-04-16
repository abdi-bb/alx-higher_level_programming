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
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getter for size attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size attribute'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''That assigns multiple arguments to the attributes'''
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.width = v
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        '''Dictionary representation of a Square'''
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
