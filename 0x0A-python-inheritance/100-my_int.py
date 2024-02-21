#!/usr/bin/python3
"""
class MyInt
"""

class MyInt(int):
    def __eq__(self, other):
        """ Overrides the __eq__ operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Overrides the __ne__ operator """
        return super().__eq__(other)
