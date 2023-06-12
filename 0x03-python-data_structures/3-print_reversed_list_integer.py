#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = []
    if len(my_list) == 0:
        return "None"
    for i in range(len(my_list) - 1, -1, -1):
        new_list.append(my_list[i])
        print("{:d}".format(my_list[i]))
    return new_list
