#!/usr/bin/python3
"""
This Module of the class MyList
"""


class MyList(list):
    """
    This is class MyList that inherits from list
    """

    def print_sorted(self):
        """
        This function prints a list, but sorted (ascending sort)

        Args:
            self
        """
        print(sorted(self))
