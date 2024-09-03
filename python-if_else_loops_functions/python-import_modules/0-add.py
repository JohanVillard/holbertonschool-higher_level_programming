#!/usr/bin/python3
"""
Adds two numbers and prints the result.

This script imports the `add` function from the module `add_0` and uses it
to add two predefined integers, `a` and `b`. The result of the addition
is then printed in the format "a + b = result".
"""

from add_0 import add

a = 1
b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
