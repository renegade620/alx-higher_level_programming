#!/usr/bin/python3
""" save object to file """
import json


def save_to_json_file(my_obj, filename):
    """write object to file using JSON """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
