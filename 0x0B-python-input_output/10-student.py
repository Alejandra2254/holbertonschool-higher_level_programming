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
        """Returns dictionary"""
        flag = False
        if (type(attrs) is list):
            flag = True
            for attr in attrs:
                if type(attr) is not str:
                    flag = False
        if flag is True:
            my_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
        else:
            my_dict = self.__dict__.copy()

        return my_dict
