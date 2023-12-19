#!/usr/bin/python3
""" define a class named Square """


class Square:
    """ Represent a Square """

    def __init__(self, size=0):
        """
        Initialize a new Square

        Args:
             size (int): The size of the new square
        """
        self.size = size

    def area(self):
        """calculate the area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstances(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
