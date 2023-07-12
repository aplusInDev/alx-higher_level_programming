#!/usr/bin/python3
"""
This Module of the function to_json_string()
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string):
    """
    return json.dumps(my_obj)
