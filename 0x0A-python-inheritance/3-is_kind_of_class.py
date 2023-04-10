#!/usr/bin/python3

'''
module name: '3-is_kind_of_class'
contained functions:
    is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''
    checks instance of an objecet

    Return:
        True if obj is instance of a specified class or superclass of
        the specified class or returns False if not
    '''
    return isinstance(obj, a_class)
