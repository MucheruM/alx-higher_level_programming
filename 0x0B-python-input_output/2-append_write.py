#!/usr/bin/python3
"""A function that a's str to end of txt file & returns num of char added"""


def append_write(filename="", text=""):
    """
    Appends a str at the end of text file and returns the num of char added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The str to append.
    Return:
        The num of char appended.
    """
    with open(filename, "a", encoding="utf-8") as fil_e:
        return fil_e.write(text)
