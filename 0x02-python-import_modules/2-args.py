#!/usr/bin/python3
import sys

if _name_ == "_main_":

    a = len(sys.argv)
    
    if a == 1 or a > 2:
        b = "b"
    else:
        ""

    if a > 1:
        c = ":"
    else:
        "."

        print("{:d} argument{}{}".format(a - 1, b, c))

        for i in range(1, a):
            print("{:d}: {}".format(i, sys.argv[i]))
