#!/usr/bin/python3
"""define a studen class"""


class Student():
    """a class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """Student constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns dictionary description of json object.'''
        if hasattr(self, "__dict__"):
            return self.__dict__.copy()
        else:
            return {}
