#!/usr/bin/python3
"""This module defines the class 'MyList'"""


class MyList(list):
    """Represent a list of integers, inherited from Python's list."""

    def print_sorted(self):
        """
        Sort and print the list in ascending order.

        The list is sorted without modifying the original list.

        Returns:
            None: The function prints the sorted list.
        """
        print(sorted(self))
