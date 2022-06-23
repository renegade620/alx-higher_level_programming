#!/usr/bin/python3
"""Printing square """


class Square:
    """defines a square """
    def __init__(self, size=0):
        """ init square

        Args:
            size: square size

        """
        self.size = size

    def area(self):
        """ area of square """
        return self.__size * self.__size

    @property
    def size(self):
        """ getter for __Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for __size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """ squae area printing """
        for i in range(self.__size):
            print("#" * self.__size)
        if (self.__size == 0):
            print()
