#!/usr/bin/python3
""" Defines a func that w's an Obj to a txt file, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a python object to a JSON file.

    Arg:
       my_obj: The python file to be saved to the JSON file.
       filename (str): The name of the file where the obj is saved.
    """
    with open(filename, "w") as fil_e:
        json.dump(my_obj, fil_e)
