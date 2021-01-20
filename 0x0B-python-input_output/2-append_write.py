#!/usr/bin/python3
"""module to append in a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding='utf-8') as ale_file:
        num = ale_file.write(text)
    return num
