#!/usr/bin/python3
"""
This Module for the function ()
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str): name of file
        text (str): content to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
