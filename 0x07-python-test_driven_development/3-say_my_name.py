#!/usr/bin/python3
"""
Define a Say my name function
"""


def say_my_name(first_name, last_name=""):
    """prints name

    first arg: string that prints first name
    second arg: string that prints last name

    Raises:
        TypeError(both must be a string)
    """
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
