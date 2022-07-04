#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ empty class """

    def area(self):
        """ not implemented, raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks if value is an integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
