#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = sorted(a_dictionary)
    for x in s:
        print("{}: {}".format(x, a_dictionary[x]))
