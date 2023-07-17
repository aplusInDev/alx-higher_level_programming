#!/usr/bin/python3
"""This is square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new square instance

        Args:
            size (int): square instance size
            x (int, optional): square instance x-position
            y (int, optional): square instance y-position
            id (int, optional): square instance id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get square size
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set square size
        """
        self.value_validator("width", size)
        self.width = size
        self.height = size

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>
        """
        s = "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width
        )
        return s

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public
        getter and setter size

        Args:
            *args: Variable-length arguments representing attribute values.
            **kwargs: Keyword arguments representing attribute-value pairs.
        Returns:
            nothing
        """
        if len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
            return
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
