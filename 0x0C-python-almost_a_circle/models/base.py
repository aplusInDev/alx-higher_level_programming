#!/usr/bin/python3
"""This is base module
"""
import json
import csv
from turtle import *

"""
import turtle
"""


class Base:
    """This class will be the `base` of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)

    Attributes:
        id (int): new instance identifier
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance

        Args:
            id (int, optional): new instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of objects to be saved.
        """
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(cls.to_dictionary(obj))
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): The JSON string to be deserialized.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary (dict): Keyword arguments representing
            the attributes of the object.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                string = f.read()
                lst = cls.from_json_string(string)
                inst = []
                for item in lst:
                    inst.append(cls.create(**item))
                return inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV
        Args:
            list_objs (list): A list of objects to be written to the CSV file.
        """
        with open(cls.__name__ + ".csv", "w") as f:
            wr = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    wr.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    wr.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV
        """
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                rd = csv.reader(f)
                inst = []
                r_keys = ["id", "width", "height", "x", "y"]
                s_keys = ["id", "size", "x", "y"]
                data = {}
                for row in rd:
                    if cls.__name__ == "Rectangle":
                        for key, value in zip(r_keys, row):
                            data[key] = int(value)
                    else:
                        for key, value in zip(s_keys, row):
                            data[key] = int(value)
                    inst.append(cls.create(**data))
                return inst
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): List of Rectangle objects.
            list_squares (list): List of Square objects.
        """
        d = Turtle()
        color_list = ["red", "orange", "yellow", "green", "blue", "balck"]
        i = 0
        for obj in list_rectangles:
            if i >= len(color_list) - 1:
                i = 0
            draw_2(d, color_list[i], obj.x, obj.y, obj.width, obj.height)
            i += 1
        for obj in list_squares:
            if i >= len(color_list) - 1:
                i = 0
            draw_2(d, color_list[i], obj.x, obj.y, obj.size, obj.size)
            i += 1
        done()


def draw_2(d, color, x, y, width, height):
    """opens a window and draws all the Rectangles and Squares

        Args:
            d: first parameter
            color: rectangle color
            x: rectangle x-position
            y: rectangle y-position
            width: rectangle width
            height: rectangle height
        """
    d.color(color)
    # d.begin_fill()
    d.penup()
    d.goto(x, y)
    d.pendown()
    for _ in range(2):
        d.forward(width)
        d.right(90)
        d.forward(height)
        d.right(90)
    # d.end_fill()
