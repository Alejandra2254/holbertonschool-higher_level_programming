#!/usr/bin/python3
"""
write a function that prints
format My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ Function that say my name
    both arguments have to be strings """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
