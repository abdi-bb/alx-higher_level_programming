#!/usr/bin/python3

'''
module: '4-from_json_string'
funcs:
    from_json_string
'''

import json


def from_json_string(my_str):
    '''
    Returns python data structure from json string.
    '''
    return json.load(my_str)
