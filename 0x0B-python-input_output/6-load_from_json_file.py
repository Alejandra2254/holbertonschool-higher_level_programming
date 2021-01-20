#!/usr/bin/python3
"""module to load from json file"""
import json


def load_from_json_file(filename):
    """function that creates an Object
    from a “JSON file”"""
    with open(filename, encoding='utf-8') as a_file:
        line = a_file.readline()
        new_object = json.loads(line)
    return new_object
