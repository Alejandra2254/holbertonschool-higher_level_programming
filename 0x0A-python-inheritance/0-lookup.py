#!/usr/bin/python3
"""Function that returns a list of attributes"""


def lookup(obj):
    """
    Function that returns a list of available attributes
    and methods of an object
    """
    return dir(obj)
