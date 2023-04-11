#!/usr/bin/python3

'''
Module name: '9-student'
Functions:
    student
'''


class Student:
    '''Represents class Student'''

    def __init__(self, first_name, last_name, age):
        '''Instantiates new Student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns json string'''
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
