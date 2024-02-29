#!/usr/bin/python3
"""
A base model class.
"""


class Base:
    """
    Base model.
    Represents the "base" for all other classes
    Attributes:
        __nb_objects(int): Number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base
        Args:
            id(int): ID of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
