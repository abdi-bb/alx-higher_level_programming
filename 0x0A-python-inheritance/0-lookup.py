#!/usr/bin/python3

'''
module name: '0-lookup'
functions contained: lookup
'''


def lookup(obj):
    '''
    Returns available attributes and methods of an object.

    Args:
        obj (object) - object to print its attributes and methods

    Return:
        list of attributes and methods of object obj
    '''
    return sorted([attr for attr in dir(obj) if not callable(
        getattr(obj, attr))] + [method for method in dir(
            obj) if callable(getattr(obj, method))])
