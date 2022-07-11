#!/usr/bin/python3
""" Base class """

import json
import csv
import os
import turtle


class Base:
    """ defines Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

