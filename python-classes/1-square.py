#!/usr/bin/python3
"""This module defines the 'Square' class."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """
        Initialize a new square instance.

        Parameters:
            size (int): The size of one side of the square.
                        No type/value verification.
        """
        self._size = size
