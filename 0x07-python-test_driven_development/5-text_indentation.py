#!/usr/bin/python3
"""
Write a function that prints a
text with 2 new lines after each of these characters
"""


def text_indentation(text):
    """ Identation with these characters
    these characters: ., ? and : """
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("")
            print("")
            i += 1
        i += 1
