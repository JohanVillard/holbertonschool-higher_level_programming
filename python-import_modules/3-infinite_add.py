#!/usr/bin/python3

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
