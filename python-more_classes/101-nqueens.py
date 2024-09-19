#!/usr/bin/python3
import sys

"""
This module solves the N queens problems.

Usage: nqueen N
"""


class Queen:
    """ """

    def __int__(self, row=0, col=0, next=None, prev=Node):
        """ """
        self.row = row
        self.col = col
        self.next = next
        self.prev = prev


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueen N")
        sys.exit(1)

    # Cast argv[1] into integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create N queen(s)
    queen_ + 1 = Queen(row, col)

# root(P): Return the partial candidate at the root of the search tree

# reject(P, c): Return true only if the partial candidate c is not worth completing

# accept(P, c) return true if c is a solution of P, and false otherwise.

# first(P, c): 
