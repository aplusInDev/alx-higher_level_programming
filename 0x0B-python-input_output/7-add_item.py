#!/usr/bin/python3
"""
This  Module adds all arguments to Python list,
and then save them to a file
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Load the existing list from the file or create a new one
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

# Add all arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the list to the file as a JSON representation
save_to_json_file(my_list, "add_item.json")
