#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangl
"""
class Rectangle:
    """
    Class Rectangle with attributes width and height
    """
    def __init__(self, width=0, height=0):
        """constructor function"""
        self.width = width
        self.heigth = height

    @property
    def width(self):
        """Method recover the value Width Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method Evalute the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise typeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Method recover the value height Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that set the value of height attribute"""
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise typeError("heigth must be an integer")
        self.__height = value
