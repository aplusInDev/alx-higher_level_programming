#!/usr/bin/python3
""" this module create Square class """


class Square:
    """ Square class """

    def __init__(self, size=0):
        """ initialize Square class """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculate Square class area """
        return self.__size ** 2
