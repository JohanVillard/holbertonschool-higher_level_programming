#!/usr/bin/python3
"""
Prints numbers from 0 to 98 along with their hexadecimal equivalents.

This script iterates through numbers from 0 to 98 and prints each number
followed by its corresponding hexadecimal value
in the format "number = hex(number)".
"""

for i in range(0, 99):
    print("{} = {}".format(i, hex(i)))
