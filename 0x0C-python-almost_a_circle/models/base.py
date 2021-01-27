#!/usr/bin/python3
"""file to create Base class"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        the JSON string representation of list_dictionaries
        """
        if (list_dictionaries is not None and type(list_dictionaries) is list):
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of
        list_objs to a file
        """
        if (list_objs is None or
                list_objs == [] or
                type(list_objs) is not list):
            json_str = json.dumps([])
        else:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            json_str = Base.to_json_string(list_dicts)
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        static method from json string
        """
        if json_string is not None and type(json_string) is str:
            list_j = json.loads(json_string)
        else:
            list_j = []
        return list_j

    @classmethod
    def create(cls, **dictionary):
        """
        that returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
            tmp.update(**dictionary)
        if cls.__name__ == "Square":
            tmp = cls(1)
            tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """
        that returns a list of instances
        """
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                fread = f.read()
                list = Base.from_json_string(fread)
                create = []
                for i in list:
                    create.append(cls.create(**i))
                return create
        except FileNotFoundError:
            return []
