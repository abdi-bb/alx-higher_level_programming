#!/usr/bin/python3

'''
module name: '2-is_same_class'
contained functions:
    is_same_class
'''


def is_same_class(obj, a_class):
    '''
    checks class of an object

    Args:
        obj (to be checked) - object to check its instance
        a_class (to check with) - given instance

    Return:
        Boolian (True if they are exactly the same instances otherwise False)
    '''
    return type(obj) == a_class
