#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers

    Parameters:
        a(int/float): First int/float
        b(int/float): Second int/float. Default vale is 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: If a or b is not an int/float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
