#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        """init

        Args:
            width: width of rectangle
            height: length of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self._width = value

    @property
    def height(self):
        """height getter """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self._height = value

    @def area(self):
        """ rectangle area """
        return self.__width * self.__height

    @def perimeter:
        """ rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
