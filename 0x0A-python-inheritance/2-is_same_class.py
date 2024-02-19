#!/usr/bin/python3
"""
Exact same object
"""


def is_same_class(obj, a_class):
    """
    Returns:True - if is an instance of object
            False - otherwise
    """
    return (type(obj) is a_class)
