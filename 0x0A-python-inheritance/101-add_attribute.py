#!/usr/bin/python3

'''
Module name: '101-add_attribute'
contained functions:
    add_attribute
'''


def add_attribute(obj, attr_name, attr_value):
    '''
    Adds attribute if possible
    '''
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
