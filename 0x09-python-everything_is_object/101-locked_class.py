#!/usr/bin/python3
"""
This Module contains lockedClass
"""


class LockedClass:
    """
    class LockedClass
    Prevents any attributs other than first_name
    """
    __slots__ = ["first_name"]
