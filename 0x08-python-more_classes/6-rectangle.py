#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init

        Args:
            width: width of rectangle
            height: length of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ represents rectangle in print """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
    return("".join(rect))

    def __repr__(self):
        """ string representation of rectangle """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """ deletion of rectangle """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
