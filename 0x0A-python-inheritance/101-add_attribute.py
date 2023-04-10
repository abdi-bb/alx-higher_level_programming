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
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] == attr_value
