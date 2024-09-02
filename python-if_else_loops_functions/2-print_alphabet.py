#!/usr/bin/python3
"""
Prints the lowercase alphabet using a loop.

This script iterates over the ASCII values of the lowercase alphabet
(from 'a' to 'z') and prints each character on the same line without spaces.
"""

for i in range(97, 123):
    print(chr(i), end="")
