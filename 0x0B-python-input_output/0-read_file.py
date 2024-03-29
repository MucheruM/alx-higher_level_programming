#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads contents of a file and print to stdout

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, encoding="utf-8") as fil_e:
        print(fil_e.read(), end="")
