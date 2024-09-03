#!/usr/bin/python3
"""
Prints the lowercase alphabet in a single line without a newline.

This script iterates over the ASCII values for lowercase letters
(from 'a' to 'z') and prints each character on the same line using
a single print function without adding any trailing newline.
"""

# Create a string containing all lowercase letters
for i in range(97, 123):
    print("{}".format(chr(i)), end="")
