#!/usr/bin/python3
"""Creating Rectangle class, 
that inheritance from base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """method constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method to recover value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to evaluate width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Method to recover value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to evaluate height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method to recover value of x"""
        return self.__X

    @x.setter
    def x(self, value):
        """Method to evaluate x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method recover the value Width Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method Evaluate the value of width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """ public method that returns the area 
        value of the Rectangle instance."""
        return self.__width * self.__height
    
    def display(self):
        """public method that prints in stdout the
        Rectangle instance with the character #"""
        display = ""
        tmp = self.__x
        for i in range(self.__height):
            if self.__y != 0:
                print("\n")
                self.__y = 0
            for j in range(self.__width):
                if self.__x != 0:
                    display += self.__x * " "
                    self.__x = 0
                display += "#"
            display += "\n"
            self.__x = tmp
        display = display[:-1]
        print("{}".format(display))

    def __str__(self):
        """
        Print an Unofficial string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
    
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
                self.width = arg
            elif i == 3:
                self.height = arg
            elif i == 4:
                self.x = arg
            elif i == 5:
                self.y = arg
            else:
                break
        if i == 0:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
                else:
                    break