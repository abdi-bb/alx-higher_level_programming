#!/usr/bin/python3

'''
Module name: '5-save_to_json_file'
funcs:
    save_to_json_file
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    writes to a text file using json representation
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
