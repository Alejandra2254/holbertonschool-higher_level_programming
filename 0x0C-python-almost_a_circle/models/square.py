#!/usr/bin/python3
"""Creating Square class,
that inheritance from base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inheritance from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Method constructor"""
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def __str__(self):
        """
        print an unofficial string
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
    