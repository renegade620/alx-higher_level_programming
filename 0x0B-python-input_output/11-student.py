#!/usr/bin/python3
""" Student to disk and reload """


class Student:
    """ defines student """
    def __init__(self, first_name. last_name, age):
        """init new student """
        self.first_name = first_name
        slef.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attr)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        for k, x in json.items():
            setattr(self, k, x)
