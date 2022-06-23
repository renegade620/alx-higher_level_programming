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
        self.position = position

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
        if (self.__size == 0):
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @position.setter
    def position(self, value):
        """ setter of __Position """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of \
                       2 positive integers")
        else:
            self.__position = value
