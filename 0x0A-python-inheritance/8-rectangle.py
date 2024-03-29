#!/usr/bin/python3
"""
Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rep of a rectangle
    """
    def __init__(self, width, height):
        """
        Instantiation
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
