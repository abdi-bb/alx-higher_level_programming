#!/usr/bin/python3

'''
module name: '4-print_square'
functions contained:
    'print_square(size)
'''


def print_square(size):
    '''Prints a square with char #


    Args:
        size (int): size of the square

    Raise:
        TypeError, ValueError

    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size > 0:
        for i in range(size):
            [print('#', end='') for j in range(size)]
            print()
