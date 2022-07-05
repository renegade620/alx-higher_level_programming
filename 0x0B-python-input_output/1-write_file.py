#!/usr/bin/python3
""" write to a file """


def write_file(filename="", text=""):
    """ returns the number of characters written """
    with open(filename, encoding='utf-8') as ch:
        return len(ch.readlines())
