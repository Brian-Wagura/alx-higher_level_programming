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
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
