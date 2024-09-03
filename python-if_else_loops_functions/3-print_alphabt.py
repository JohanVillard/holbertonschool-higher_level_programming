#!/usr/bin/python3
"""
Prints the lowercase alphabet in a single line, excluding 'e' and 'q'.

This script iterates over the ASCII values for lowercase letters
(from 'a' to 'z'), skips the letters 'e' (ASCII 101) and 'q' (ASCII 113),
and prints the remaining letters on the same line without any trailing newline.
"""

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
