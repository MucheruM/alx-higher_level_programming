#!/usr/bin/python3
"""A class defining a rectagle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Creating an instance/object "instantiation with options h and w"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method that validates the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method that validates value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
