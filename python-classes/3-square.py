#!/usr/bin/python3
"""This module defines the 'Square' class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        Initialize a new square instance.

        Parameters:
            size (int): The size of one side of the square.
                        Must be an integer >= 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        # Private attribute
        self.__size = size

    def area(self):
        """
        Compute the area of square.

        Returns:
            the result of side * side.
        """
        return self.__size * self.__size
