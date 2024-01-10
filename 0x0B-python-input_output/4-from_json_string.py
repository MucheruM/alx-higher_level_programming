#!/usr/bin/python3
"""A function that returns an obj(Python data structure) rep by a JSON string"""
import json


def from_json_string(my_str):
    """
    Convert a JSON stiring into a Python data structure.

    Arg:
       my_str: The json string to convert into python object string.
    Return:
       str: The Python data string.
    """
    return json.loads(my_str)
