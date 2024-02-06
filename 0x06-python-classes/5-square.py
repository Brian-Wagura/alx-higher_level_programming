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

    def area(self):
        """Calculates the area of a square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrive size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
