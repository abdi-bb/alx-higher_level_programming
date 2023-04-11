#!/usr/bin/python3

'''
Module name: '8-class_to_json'
Funcs name:
    class_to_json
'''


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (object): an instance of a class whose attributes are all
        serializable

    Returns:
        A dictionary with the attributes of the object and their values.
    """
    attrs = vars(obj)
    json_dict = {}
    for attr, value in attrs.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
