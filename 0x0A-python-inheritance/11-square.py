#!/usr/bin/python3
""" This module to implement str on square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size):
        """Square constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.area()

    def __str__(self):
        """
        define str print a string unofficial
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
