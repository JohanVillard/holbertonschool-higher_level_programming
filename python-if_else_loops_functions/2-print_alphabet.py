#!/usr/bin/python3
"""
Prints the lowercase alphabet in a single line.

This script generates a string with all lowercase letters
(from 'a' to 'z') and prints it using a single print function,
without any trailing newline.
"""

# Create a string containing all lowercase letters
print("".join(chr(i) for i in range(97, 123)), end="")
