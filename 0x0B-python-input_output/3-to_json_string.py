#!/usr/bin/python3

import json

'''
module: '3-to_json_string'
funcs:
    to_json_string
'''



def to_json_string(my_obj):
    '''
    Returns the JSON representation of a Python object.

    Args:
        my_obj: A Python object.

    Returns:
        A JSON string representing the object.
    '''
    return json.dumps(my_obj, sort_keys=True)

