#!/usr/bin/python3
"""
write a function that prints
format My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ Function that say my name """
    if type(first_name) not in str:
        raise TypeError("first_name must be a string")
    if type(last_name) not in str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))