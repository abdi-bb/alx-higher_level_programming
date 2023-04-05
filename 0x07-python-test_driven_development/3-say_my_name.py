#!/usr/bin/python3

'''
module: '3-say_my_name'
functions:
    'say_my_name(first_name, last_name)'
'''


def say_my_name(first_name, last_name=""):
    '''Prints name

    Args:
        first_name (str): person's first name
        last_name (str): person's last name

    Raise:
        TypeError - if either first_name or last_name are not str

    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is', first_name, last_name)
