#!/usr/bin/python3
"""A class defining a no class or attribute and prevents new instances"""


class LockedClass:
    """__slots__ locks addition of any attribute """
    __slots__ = ["first_name"]
