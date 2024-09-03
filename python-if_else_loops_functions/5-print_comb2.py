#!/usr/bin/python3
"""
Prints numbers from 0 to 99, formatted with two digits, separated by commas.

This script iterates through numbers from 0 to 99 and prints each number
formatted with two digits (e.g., '00', '01', '02', ...), followed by a comma
and a space. The last number (99) is printed without a trailing comma.
"""

for i in range(0, 100):
    print("{:02d}, ".format(i), end="")
else:
    print("{}".format(i))
