#!/usr/bin/python3
"""A function that returns the JSON rep of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Convert a Python obj to a JSON-formatted str.

    Arg:
       my_obj: The Python object to be converted.
    Return:
       str: The JSON-formatted string.
    """
    return json.dumps(my_obj)
