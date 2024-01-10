#!/usr/bin/python3
""" A function that w's a str to a txt file (UTF8) & returns the num of char"""


def write_file(filename="", text=""):
    """
    Writes str to a txt file and returns num of characters written.

    Args:
        filename (str): The name of the file to write the string.
        text (txt): The string to be written to the file.
    Return:
        int: The num of char written to the file.
    """
    with open(filename, "w", encoding="utf-8") as fil_e:
        return fil_e.write(text)
