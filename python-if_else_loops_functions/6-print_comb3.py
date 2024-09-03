#!/usr/bin/python3

for i in range(0, 10):
    n = i + 1
    if i != 8:
        for j in range(n, 10):
            print("{}".format(i), end="")
            print("{}, ".format(j), end="")
    else:
        print("{}{}".format(i, j))
