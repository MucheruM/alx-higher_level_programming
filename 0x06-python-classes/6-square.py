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

    @property
    def position(self):
        """ Set the current position of the squares."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Print the square with char '#' """
        if self.__size == 0:
            print()
            return

        [print("") for j in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print(" ", end="") for j in range(0, self._position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
