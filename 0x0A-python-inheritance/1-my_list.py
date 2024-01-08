#!/usr/bin/python3
"""A function that illustrates inheritance"""


class MyList(List):
    """Class inheriting from the Superclass List"""
    def print_sorted(self):
        """Function returns a sorted dir() list"""
        print(sorted(self))
