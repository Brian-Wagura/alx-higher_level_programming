#!/usr/bin/python3
"""Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Representation of a Square
    """
    def __init__(self, size):
        """ Representation of a Square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size
