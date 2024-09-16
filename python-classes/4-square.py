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
        """
        self.__size = size  # Public attribute

    def area(self):
        """
        Compute the area of square.

        Returns:
            the result of side * side.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            The size as an integer.
        """
        return self.__size  # Private attribute

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            Value:  The size of one side of the square.
                    Must be an integer >= 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # Private attribute
