#!/usr/bin/python3

'''
Module name: 'base'
Class names:
    Base
'''

import json


class Base:
    '''Represents class Base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiation'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of JSON string representation json_string'''
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            elif cls.__name__ == 'Square':
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances.'''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**d) for d in dict_list]
        except (IOError, FileNotFoundError):
            return []
