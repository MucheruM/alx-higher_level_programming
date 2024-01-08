#!/usr/bin/python3
"""A function that illustrates inheritance"""


class MyList(list):
    """Class inheriting from the Superclass List"""
    def __init__(self):
        """Initialize the object list"""
        super().__init__()

    def print_sorted(self):
        """prints the sortd list in ascending order"""
        print(sorted(self))
