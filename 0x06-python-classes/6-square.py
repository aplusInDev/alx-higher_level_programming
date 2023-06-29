#!/usr/bin/python3
""" this module create Square class """


class Square:
    """ Square class """

    def __init__(self, size=0, position=(0, 0)):
        """ initialize Square class """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ get Square class size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set Square class size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ get Square class position """
        return self.__position

    @position.setter
    def position(self, value):
        """ set Square class position """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) \
                or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ calculate Square class area """
        return self.__size ** 2

    def my_print(self):
        """ print Square class """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print("#", end='')
            print()
