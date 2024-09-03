#!/usr/bin/python3
"""
Sums up all the command-line arguments and prints the result.

This script takes command-line arguments (expected to be integers),
sums them up, and prints the total. If no arguments are provided,
it will print 0.

The functionality is executed only if the script is run directly,
not when imported as a module.
"""

from sys import argv

if __name__ == "__main__":
    total_arg = len(argv) - 1

    if total_arg != 0:
        result = 0
        i = 1
        for arg in argv[1:]:
            result += int(arg)
            i += 1

    print(f"{result}")
