#!/usr/bin/python3
'''Defines an integer addition function'''


def add_integer(a, b=98):
    '''
    Returns the additions of two integers.

    Args:
        a (int or float): The first integer
        b (int or float): The second integer

    Return:
        The addition of a and b

    Raises:
        TypeError: If a or b not an integer or float
    '''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
