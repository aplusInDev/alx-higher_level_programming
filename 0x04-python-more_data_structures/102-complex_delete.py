#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for k, v in a_dictionary.items():
        if value is v:
            my_list.append(k)
    for i in reversed(my_list):
        del a_dictionary[i]
    return a_dictionary
