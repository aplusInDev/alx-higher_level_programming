#!/usr/bin/python3
""" this module create Square class """


class Square:
    """ initialize Square class """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
