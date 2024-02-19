#!/usr/bin/python3
"""
Class list
"""


class MyList(list):
    """
    MyList ingerits from parent list
    """
    def print_sorted(self):
        """
        Print sorted list
        """
        print(sorted(self))
