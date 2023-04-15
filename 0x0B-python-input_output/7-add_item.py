#!/usr/bin/python3

"""
Adds all arguments to a Python list and saves them to a JSON file
"""

import sys
import json
from os import path
from typing import List

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str], filename: str):
    """
    Adds all arguments to a Python list and saves them to a JSON file

    :param args: List of strings to add to the list
    :param filename: Name of the JSON file to save the list to
    :return: None
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in args:
        my_list.append(arg)

    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    args = sys.argv[1:]
    add_item(args, "add_item.json")
