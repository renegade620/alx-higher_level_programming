#!/usr/bin/python3
""" class Rectangle inherits class BaseGeometry """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits class BaseGeometry """

    def __init__(self, width, height):
        """ init new rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ rectangle description """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
