#!/usr/bin/python3
"""
Geometry modules
"""


class BaseGeometry:
    """ An empty class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates whether the value is an integer or less than
        or equal to zero
        name is always a string
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
