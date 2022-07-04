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
