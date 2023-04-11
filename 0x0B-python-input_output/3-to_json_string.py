#!/usr/bin/python3

import json

'''
module: '3-to_json_string'
funcs:
    to_json_string
'''


def to_json_string(my_obj):
    '''
    Returns json representation of an object(string).
    '''
    return json.dumps(my_obj)
