#!/usr/bin/python3
"""Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square
    """
    def __init__(self, size):
        super().__init__(size, size)
