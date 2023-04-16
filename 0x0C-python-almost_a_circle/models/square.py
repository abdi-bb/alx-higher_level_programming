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
