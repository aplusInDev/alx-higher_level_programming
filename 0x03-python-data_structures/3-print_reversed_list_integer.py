#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    for i in range(l):
        print(my_list[l - 1 - i], end="\n")
