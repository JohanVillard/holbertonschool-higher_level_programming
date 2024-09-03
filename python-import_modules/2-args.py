#!/usr/bin/python3
"""
Handles and prints command-line arguments.

This script counts and displays the number of cmd-line arguments passed to it.
It prints a message indicating whether there are no arguments, one argument, or
multiple arguments. If there are any arguments, it then lists each argument
with its corresponding index.

This functionality is wrapped in an `if __name__ == "__main__":`
block to ensure it only runs when the script is executed directly.
"""

from sys import argv

if __name__ == "__main__":
    total_arg = len(argv) - 1

    if total_arg == 1:
        print(f"{len(argv) - 1} argument:")
    elif total_arg == 0:
        print(f"{len(argv) - 1} arguments.")
    elif total_arg > 0:
        print(f"{len(argv) - 1} arguments:")

    if total_arg != 0:
        i = 1
        for arg in argv[1:]:
            print(f"{i}: {arg}")
            i += 1
