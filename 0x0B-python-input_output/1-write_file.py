#!/usr/bin/python3
""" A function that w's a str to a txt file (UTF8) & returns the num of char"""


def write_file(filename="", text=""):
    """
    Writes str to a txt file and returns num of characters written.

    Args:
        filename (str): The name of the file to read the string.
        text (txt): The name of the file to write the string.
    Return:
        The num of char written
    """
    with open(filename, "w", encoding="utf-8") as fil_e:
        return fil_e.write(text)
