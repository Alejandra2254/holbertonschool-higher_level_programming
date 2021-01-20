#!/usr/bin/python3
"""This module to open a file"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout"""
    with open(filename, "r") as f:
        print("{}".format(f.read()), end="")
