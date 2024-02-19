#!/usr/bin/python3
"""
Full rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


def Rectangle(BaseGeometry):
    """
    Rectangle using BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validation("height", height)
        self.__height = height

    def area(self):
        """ Calculates and returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle """
        return f"[Rectangle] {self.__width} / {self.__height}"
