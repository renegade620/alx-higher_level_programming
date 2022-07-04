#!/usr/bin/python3
""" Same class or inherited """


def is_kind_of_class(obj, a_class):
    """ checks if an object is an instance or an inherited instance
    of a class """
    if isinstance(obj, a_class):
        return True
    return False
