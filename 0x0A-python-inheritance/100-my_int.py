#!/usr/bin/python3
"""
This Module of the class MyInt that inherits from int
"""


class MyInt(int):
    """
    This class is a rebel, has == and != operators inverted
    """

    def __init__(self, value):
        """
        Initializing value
        """
        self.value = value

    def __eq__(self, other):
        """
        This function Returns invert of ==
        """
        return self.value != other

    def __ne__(self, other):
        """
        This function Returns invert of !=
        """
        return self.value == other
