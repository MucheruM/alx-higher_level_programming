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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Set the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Print the square with char '#' """
        if self.__size == 0:
            print()
            return
        for j in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
