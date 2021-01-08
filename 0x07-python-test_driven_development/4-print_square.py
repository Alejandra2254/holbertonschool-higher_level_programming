#!/usr/bin/python3
"""
Function that prints a square with the character
"""



def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range (0, size):
        for j in range(0, size):
            print("#", end = "")
        print("")
