#!/usr/bin/python3
""" simple inheritance """


class MyList(list):
    """ inherited Class list """
    def print_sorted(self):
        """ prints sorted list """
        print(self(sorted))
