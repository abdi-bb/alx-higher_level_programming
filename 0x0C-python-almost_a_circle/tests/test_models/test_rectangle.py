#!/usr/bin/python3
'''Unittest for Rectangle class'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Test cases for Rectangle class'''

    def test_init(self):
        '''Test instantiation of Rectangle class'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        '''Test width attribute'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1.width = 'hello'
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1.width = -10

    def test_height(self):
        '''Test height attribute'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1.height = 'hello'
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r1.height = -10

    def test_x(self):
        '''Test x attribute'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1.x = 'hello'
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r1.x = -10

    def test_y(self):
        '''Test y attribute'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1.y = 'hello'
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r1.y = -10

    def test_area(self):
        '''Test area method'''
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

    def test_display(self):
        '''Test display method'''
        pass

    def test_str(self):
        '''Test __str__ method'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

    def test_update(self):
        '''Test update method'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 2/1 - 4/6')
        r1.update(89, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 2/1 - 3/6')
        r1.update(89, 3, y=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 2/4 - 3/6')
        r1.update(x=12)
        self.assertEqual(str(r1), '[Rectangle] (89) 12/4 - 3/6')
        
    def test_to_dictionary(self):
      '''Test to_dictionary method'''
      r1 = Rectangle(4,6,id=12,x=2,y=5)
      expected_dict = {'id':12,'width':4,'height':6,'x':2,'y':5}
      actual_dict = r1.to_dictionary()
      self.assertDictEqual(expected_dict , actual_dict)

if __name__ == '__main__':
    unittest.main()
