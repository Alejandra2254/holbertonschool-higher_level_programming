#!/usr/bin/python3
class BaseGeometry:
    """class BaseGeometry based on task 5 but with
    other instances"""
    def area(self):
        """
        public instance method: def area(self): that raises
        an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
