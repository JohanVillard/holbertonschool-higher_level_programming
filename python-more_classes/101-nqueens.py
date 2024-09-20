#!/usr/bin/python3

"""
This module solves the N queens problems.

Usage: nqueen N
"""

import sys


class Board:
    """
    Represent a chess board for solving the N-Queens problem.

    The Board class stores the current state of the board, tracks solutions,
    and helps in placing queens on the board following the N-Queens rules.
    """

    def __init__(self, N=0):
        """
        Initialize the Board with a given number of queens.

        Parameters:
            N (int): The number of queens to place on the board.
                     The minimum value is 4 for the classic N-Queens problem.

        Attributes:
            current_solution (list): A list representing the current position
                                     of queens on the board. Each index
                                     represents a row, and the value at that
                                     index represents the column where the
                                     queen is placed.
            solutions (list): A list of all valid solutions found. Each
                              solution is a list similar to `current_solution`,
                              where the index represents a row, and the value
                              represents the column of a queen.
        """
        # index of list = row --- value at index = col
        self.current_solution = [0 for x in range(N)]
        # List to store all valid solutions
        self.solutions = []

    def is_safe(self, test_row, test_col):
        """
        Check whether the current queen is under attack.

        A queen is considered "under attack" if another queen is in the same
        column or on the same diagonal.

        Parameters:
            test_row (int): The row to test for placing the queen.
            test_col (int): The column to test for placing the queen.

        Returns:
            bool: True if placing the queen at (test_row, test_col) is
                  safe from any attacks, otherwise False.
        """
        # No need to check if it's the first row,
        # as no queens have been placed yet.
        if test_row == 0:
            return True

        # Check against all previously placed queens
        for row in range(0, test_row):
            # Check if there's a queen in the same column
            if test_col == self.current_solution[row]:
                return False

            # Check if the queen is on the same diagonal
            # A diagonal attack happens when the absolute difference in rows
            # equals the absolute difference in columns.
            if abs(test_row - row) == abs(test_col - self.current_solution[row]):
                return False

        # If no conflicts were found, the queen is safe
        return True

    def place_queen(self, row):
        """
        Recursively search for safe positions to place queens on the board.

        This method attempts to place a queen in a safe position for the given
        row and continues to place queens in subsequent rows, using
        backtracking to find all possible solutions for the N-Queens problem.

        Parameters:
            row (int): The row on which to attempt placing a queen.

        Returns:
            None: This method does not return a value. When the recursion
            completes, all valid solutions are stored in the `self.solutions`
            list.
        """
        for col in range(N):
            # Check if placing the queen at (row, col) is safe
            if not self.is_safe(row, col):
                continue
            else:
                # Place the queen in the current column
                self.current_solution[row] = col
                if row == N - 1:
                    # If this is the last row, a solution has been found
                    self.solutions.append(self.current_solution.copy())
                else:
                    # Move to the next row and attempt to place the next queen
                    self.place_queen(row + 1)

    def __str__(self):
        """
        Return a string repr of the solutions for the N-Queens problem.

        This method prints the number of solutions found and constructs a list
        representing the positions of the queens in each solution. Each queen's
        position is represented as a pair of integers [row,col], where `row` is
        the index in the solution (the row on the board) and `col` is the value
        at that index (the column where the queen is placed).

        For debugging purposes, the method also prints out each solution.

        Returns:
            str: An empty string
                 (the main purpose of this method is to print the solutions).
        """
        solution_lst = []
        valid_queen = []

        for solution in self.solutions:
            for idx, col in enumerate(solution):
                valid_queen.extend([idx, col])
                solution_lst.append(valid_queen)
                valid_queen = []
            print(solution_lst)
            solution_lst = []

        return ""


if __name__ == "__main__":
    # Check if the numbers of args is good
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Cast argv[1] into integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is more than 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an instance of Board with N Queens
    new_board = Board(N)

    # Launch the search of solutions by placing the first queen
    new_board.place_queen(0)

    # Print the solutions
    print(new_board)
