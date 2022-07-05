#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ object from JSON """
    with open(filename) as f:
        return json.load(f)
