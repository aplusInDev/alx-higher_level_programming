#!/usr/bin/python3
""" this module create Square class """


class Square:
    """ Square class """

    def __init__(self, size=0):
        """ initialize Square class """
        self.__size = size

    @property
    def size(self):
        """ get Square class """
        return self.__size

    @size.setter
    def size(self, value):
        """ set Square class """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculate Square class area """
        return self.__size ** 2

    def my_print(self):
        """ print Square class """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
