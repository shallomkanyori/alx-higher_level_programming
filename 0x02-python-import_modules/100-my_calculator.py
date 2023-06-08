#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    sys.exit(0)

args = sys.argv

if len(args) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(args[1])
b = int(args[3])
operator = args[2]

if operator == "+":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
elif operator == "-":
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
elif operator == "*":
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
elif operator == "/":
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
