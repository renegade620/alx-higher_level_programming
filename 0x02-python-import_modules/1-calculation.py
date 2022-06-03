#!/usr/bin/python3
from calculator_1 import div, mul, add, sub

if  _name_ == "_main_":

    a = 10
    b = 5

    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
