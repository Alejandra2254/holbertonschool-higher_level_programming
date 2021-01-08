#!/usr/bin/python3
"""
Function that add to integers or floats
Return the add
"""


def add_integer(a, b=98):
    """
    Function add_integer
    a y b as integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
