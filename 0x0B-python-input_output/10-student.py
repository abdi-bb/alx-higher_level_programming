#!/usr/bin/python3

'''
module: '10-student'
Class:
    Student
'''


class Student:
    '''Represents class student'''

    def __init__(self, first_name, last_name, age):
        '''Instantiates new student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
