#!/usr/bin/python3
"""
This Module for the function append_write()
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): name of file
        text (str): content to be appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
