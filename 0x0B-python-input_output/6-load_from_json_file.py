#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Arg:
       filename:
    Return:

    """
    with open(filename) as fil_e:
        return json.load(fil_e)
