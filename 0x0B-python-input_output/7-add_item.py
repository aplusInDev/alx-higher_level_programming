#!/usr/bin/python3
"""
This  Module adds all arguments to Python list,
and then save them to a file
"""
from sys import argv

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
exist = []
exist.extend(load_from_json_file("add_item.json"))
exist.extend(argv[1:])
save_to_json_file(exist, "add_item.json")
