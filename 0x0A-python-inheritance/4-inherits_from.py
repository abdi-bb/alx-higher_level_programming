#!/usr/bin/python3

'''
Module name: '4-inherits_from'
Contained functions:
    inherits_from
'''


def inherits_from(obj, a_class):
    '''
    Checks subclass
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
