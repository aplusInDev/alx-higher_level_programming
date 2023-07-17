#!/usr/bin/python3
"""This is base module
"""


class Base():
    """This class will be the `base` of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)

    Attributes:
        id (int): new instance identifier
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise new instance
        Args:
            id (int): new instance identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
