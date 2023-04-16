#!/usr/bin/python3
'''Unittest for Base class'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test cases for Base class'''

    def test_init(self):
        '''Test instantiation of Base class'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        '''Test to_json_string method'''
        r1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r2 = {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        list_dicts = [r1, r2]
        json_list_dicts = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_list_dicts), str)

    def test_from_json_string(self):
        '''Test from_json_string method'''
        json_list_dicts = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        list_dicts = Base.from_json_string(json_list_dicts)
        self.assertEqual(type(list_dicts), list)

    def test_create(self):
        '''Test create method'''
        r1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r2 = {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        list_dicts = [r1, r2]
        instances = [Base.create(**d) for d in list_dicts]
        self.assertEqual(instances[0].__str__(), '[Rectangle] (1) 2/8 - 10/7')
        self.assertEqual(instances[1].__str__(), '[Rectangle] (2) 0/0 - 2/4')

    def test_save_to_file(self):
        '''Test save_to_file method'''
        r1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r2 = {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        list_rectangles = [Base.create(**r1), Base.create(**r2)]
        Base.save_to_file(list_rectangles)
        with open('Rectangle.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[{"id": 1,"width":10,"height":7,"x":2,"y":8},{"id":2,"width":2,"height":4,"x":0,"y":0}]')

if __name__ == '__main__':
    unittest.main()
