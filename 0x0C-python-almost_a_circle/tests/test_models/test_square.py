#!/usr/bin/python3
'''Unittest for Square class'''

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Test cases for Square class'''

    def test_init(self):
        '''Test instantiation of Square class'''
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        s2 = Square(2)
        self.assertEqual(s2.id, 2)
        s3 = Square(10, 2, 3, 12)
        self.assertEqual(s3.id, 12)

    def test_size(self):
        '''Test size attribute'''
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1.size = 'hello'
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.size = -10

    def test_x(self):
        '''Test x attribute'''
        s1 = Square(10)
        self.assertEqual(s1.x, 0)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s1.x = 'hello'
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s1.x = -10

    def test_y(self):
        '''Test y attribute'''
        s1 = Square(10)
        self.assertEqual(s1.y, 0)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s1.y = 'hello'
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s1.y = -10

    def test_area(self):
        '''Test area method'''
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_display(self):
      '''Test display method'''
      pass

    def test_str(self):
      '''Test __str__ method'''
      s1 = Square(4,6,id=12,x=2,y=5)
      self.assertEqual(str(s1), '[Square] (12) 2/5 - 4')

    def test_update(self):
      '''Test update method'''
      s1 = Square(4,6,id=12,x=2,y=5)
      s1.update(89)
      self.assertEqual(str(s1), '[Square] (89) 2/5 - 4')
      s1.update(89,size=3)
      self.assertEqual(str(s1), '[Square] (89) 2/5 - 3')
      s1.update(89,size=3,y=4)
      self.assertEqual(str(s1), '[Square] (89) 2/4 - 3')

    def test_to_dictionary(self):
      '''Test to_dictionary method'''
      s1 = Square(4,id=12,x=2,y=5)
      expected_dict = {'id':12,'size':4,'x':2,'y':5}
      actual_dict = s1.to_dictionary()
      self.assertDictEqual(expected_dict , actual_dict)

if __name__ == '__main__':
    unittest.main()
