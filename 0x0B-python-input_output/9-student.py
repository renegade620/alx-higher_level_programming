#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ defines student """
    def __init__(self, first_name. last_name, age):
        """init new student """
        self.first_name = first_name
        slef.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student """
        return self.__dict__
