#!/usr/bin/python3
"""
This Module for the function add_attribute
"""


def add_attribute(obj, attr, value):
    """
    This function adds a new attribute to an object if it's possible

    Args:
        obj: object
        attr: attribute
        value: attribute value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
