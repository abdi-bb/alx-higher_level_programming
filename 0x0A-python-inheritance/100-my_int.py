#!/usr/bin/python3

'''
Module name: '100-my_int'
Contained functions:
    my_int
'''


class MyInt(int):
    '''Represents MyInt'''

    def __eq__(self, other):
        '''inverts eq into ne '''
        return int(self) != other

    def __ne__(self, other):
        '''inverts ne in to eq'''
        return int(self) == other
