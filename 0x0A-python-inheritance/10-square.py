#!/usr/bin/python3
""" class Square inherits class Rectangle """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ defines a square """

    def __init__(self, size):
        """ init square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area of a square """
        return self.__size * self.__size
