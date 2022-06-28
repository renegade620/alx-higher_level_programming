#!/usr/bin/python3
""" addition of integers """


def add_integer(a, b=98):
    """ adds a and b. """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
