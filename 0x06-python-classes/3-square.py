#!/usr/bin/python3
""" Square Area """


class Square:
    """defines square"""

    def __init__(self, size=0):
        """
        init

        Args:
            size: square size

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """ area of square """
        return self.__size * self.__size
