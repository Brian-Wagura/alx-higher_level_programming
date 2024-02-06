#!/usr/bin/python3
"""A class Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """
        Defines size instance size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
