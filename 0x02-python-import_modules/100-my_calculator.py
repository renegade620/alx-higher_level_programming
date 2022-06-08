#!/usr/bin/python3
import sys

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <x> <operator> <z>")
        sys.exit(1)

    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    x, o, z = sys.argv[1:]

    if o == '+':
        func = add
    elif o == '-':
        func = sub
    elif o == '*':
        func = mul
    else:
        func = div

    print("{} {} {} = {:d}".format(x, o, z, func(int(x), int(z))))
