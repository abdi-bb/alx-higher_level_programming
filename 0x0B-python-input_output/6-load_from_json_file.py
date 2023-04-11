#!/usr/bin/python3

'''
Module name: '6-load_from_json_file'
Functions:
    load_from_json_file
'''

import json


def load_from_json_file(filename):
    '''
    Creates object from JSON file.
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        data = json.load(f)
    return data
