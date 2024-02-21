#!/usr/bin/python3
"""
Adds a new attribute to an object
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object

    Args:
        obj: object
        attr_name: attribute name
        attr_value: attribute value
    Raises:
        TypeError: object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_name)
