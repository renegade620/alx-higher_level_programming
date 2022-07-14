#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class recttangle inherits from class base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init a rectangle """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """ get rectangle's x coordinate """
        return self.__x

    @x.setter
    def x(self, value):
        """ set rectangle's x coordinate """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get rectangle's y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ set rectangle's y coordinate """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.width * self.height

    def display(self):
        """ prints Rectangle instance """
        print("\n" * self.y, end="")
        print(" " * self.x + "#" * self.__width + "\n")

    def __str__(self):
        """ string rep of rectangle class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ rectangle update """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k = "y":
                    self.y = v

    def to_dictionary(self):
        """ return dict rep """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
