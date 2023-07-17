#!/usr/bin/python3
"""This is rectangle module"""

from models.base import Base


class Rectangle(Base):
    """This is rectangle class
    Attributes:
        width (int): rectangle instance width
        height (int): rectangle instance height
        x (int): rectangle instance x-position
        y (int): rectangle instance y-positions
        id (int): rectangle instance id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise new instance
        Args:
            width (int): rectangle instance width
            height (int): rectangle instance height
            x (int, optional): rectangle instance x-position
            y (int, optional): rectangle instance y-positions
            id (int, optional): rectangle instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
