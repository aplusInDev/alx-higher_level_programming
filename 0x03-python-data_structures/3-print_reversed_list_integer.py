#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    le = len(my_list)
    for i in range(le):
        print("{:d}".format(my_list[le - 1 - i]))

