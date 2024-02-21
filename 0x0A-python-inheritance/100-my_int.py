#!/usr/bin/python3
"""
class MyInt
"""

class MyInt(int):
    """
    Rebel version of an integer, perfect for opposite day
    """
    def __new__(cls, *args, **kwargs):
        """ New instance of the class """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ != is now == """
        return int(self) != other

    def __ne__(self, other):
        """ == is now != """
        return int(self) == other
