#!/usr/bin/python3
"""module write object to file with JSON"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a
    text file, using a JSON representation"""
    with open(filename, "w") as ale_file:
        json.dump(my_obj, ale_file)
