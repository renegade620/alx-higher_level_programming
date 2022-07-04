#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ checks if an object is an instance of class that either inherited
    directly or indirectly from a specified class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
