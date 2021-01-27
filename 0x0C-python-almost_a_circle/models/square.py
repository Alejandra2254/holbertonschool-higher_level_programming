#!/usr/bin/python3
"""Creating Square class,
that inheritance from base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inheritance from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Method constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Method recover the value size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Method to evaluate size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        print an unofficial string
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        public method that assigns an
        argument to each attribute
        *args: sed to send a non-keyworded variable length
        argument list to the function
        **kwargs: allows you to pass keyworded variable
        length of arguments to a function.
        """
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            elif i == 2:
                self.size = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
            else:
                break
        if i == 0:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
                else:
                    break

    def to_dictionary(self):
        """ dictionary representation of a Square"""
        dict_s = {}
        dict_s['id'] = self.id
        dict_s['x'] = self.x
        dict_s['size'] = self.size
        dict_s['y'] = self.y
        return dict_s
