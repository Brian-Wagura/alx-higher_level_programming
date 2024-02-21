#!/usr/bin/python3
"""
Only subclass of
"""


def inherits_from(obj, a_class):
    """
    Returns:True - if object is an instance of class inherited
            False - otherwise
    """
    return issubclass(type(obj), a_class)
