#!/usr/bin/python3
import sys

if __name__ == "__main__":

    a = len(sys.argv)
    b = "b" if a == 1 or a > 2 else ""
    c = ":" if a > 1 else "."
    print("{:d} argument{}{}".format(a - 1, b, c))

    for i in range(1, a):
        print("{:d}: {}".format(i, sys.argv[i]))
