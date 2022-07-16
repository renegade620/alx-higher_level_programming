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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON rep of dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON rep of list of objects to file """
        filename = cls.__name + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_d = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_d))

    @staticmethod
    def from_json_string(json_string):
        """ return list of objects rep by JSON """
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns class inst by dictionary """
        if cls.__name == "Square":
            dec = cls(5)

        if cls.__name == "Rectangle":
            dec = cls(5, 8)

        dec.update(**dictionary)
        return dec

    @classmethod
    def load_from_file(cls):
        """ returns list instance """
        list_d = []
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                s = cls.from_json_string(file.read())
            for i in s:
                list_d.append(cls.create(**i))
            return list_d
        return []

     @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rectangles and squares"""
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.shape("turtle")
            turtle.bgcolor("black")
            t.fillcolor("white")
            t.begin_fill()
            t.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                t.forward(i.width)
                t.right(90)
                t.forward(i.height)
                t.right(90)
            t.end_fill()
            turtle.done()
