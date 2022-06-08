#!/usr/bin/python3
from calculator_1 import div, mul, add, sub

if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
