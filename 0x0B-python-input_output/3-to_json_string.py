#!/usr/bin/python3

'''
module: '3-to_json_string'
funcs:
    to_json_string
'''

import json


def to_json_string(my_obj):
    '''
    Returns the JSON representation of a Python object.

    Args:
        my_obj: A Python object.

    Returns:
        A JSON string representing the object.
    '''
    return json.dumps(my_obj)
