#!/usr/bin/python3
""" This module yo create a squeare in heritance by rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size):
        """Square constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.area()
