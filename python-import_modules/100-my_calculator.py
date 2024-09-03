#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op_str = "+-*/"
        no_op = True
        for op in op_str:
            if argv[2] is op:
                no_op = False
                break

        if no_op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)

        print(f"{a} {operator} {b} = {result}")
