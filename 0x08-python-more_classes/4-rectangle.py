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

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return informal representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
