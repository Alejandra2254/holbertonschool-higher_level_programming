#!/usr/bin/python3
def lookup(obj):
    """
    Function that returns a list of available attributes
    and methods of an object
    """
    list = obj.__dict__
    return list
