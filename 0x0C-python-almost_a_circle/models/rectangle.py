#!/usr/bin/python3

'''
Module name: 'rectangle'
Class names:
    Rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''Represent class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''instantiation of Rectangle'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''returns the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Returns the height attr'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height attribute'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''gets the attribute x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets x'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''grabs y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets y'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''returns area value of rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''prints the Rectangle's area with '#' character'''
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        '''overriding the __str__ method'''
        a = self.__width
        b = self.__height
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {a}/{b}'

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''Returns the dictionary representation of the rectangle'''
        return {'id': getattr(self, "id"), 'width': getattr(
            self, "width"), 'height': getattr(self, "height"), 'x': getattr(
                self, "x"), 'y': getattr(self, "y")}
