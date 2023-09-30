#!/usr/bin/python3
"""This module contains a function that finds a peak in a list of unsorted"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    prev = 0
    for index, num in enumerate(list_of_integers):
        if index:
            prev = list_of_integers[index - 1]
        if index < len(list_of_integers) - 1:
            next = list_of_integers[index + 1]
        else:
            next = 0
        if num >= prev and num >= next:
            return num
