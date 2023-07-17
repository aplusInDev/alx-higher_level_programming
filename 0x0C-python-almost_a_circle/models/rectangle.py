#!/usr/bin/python3
"""This is rectangle module
"""
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
        self.value_validator("id", id)
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the rectangle width
        """
        self.value_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """Get the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set the rectangle height
        """
        self.value_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """Get the rectangle x-position
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Set the rectangle x-position
        """
        self.value_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """Get the rectangle y-position
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Set the rectangle y-position
        """
        self.value_validator("y", y)
        self.__y = y

    def value_validator(self, name, value):
        """
        Validate the value for a specific attribute.

        Args:
            name (str): The name of the attribute being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0 for
                    "width" or "height", or less than 0 for "x" or "y".
        """
        if value is not None and type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")
        if (name == "y" or name == "x") and value < 0:
            raise ValueError(name + " must be >= 0")

    def area(self):
        """Calculate the area of the rectangle
        Returns:
            rectangle area
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle by printing the "#" characters.
        Returns: nothing
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        s = "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.width, self.height
        )
        return s

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle object.

        Args:
            *args: Variable-length arguments representing attribute values.
            **kwargs: Keyword arguments representing attribute-value pairs.
        """
        if len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        elif len(kwargs) > 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
