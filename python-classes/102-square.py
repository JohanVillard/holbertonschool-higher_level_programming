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

    def __eq__(self, other):
        """
        Compare equality between two objects based on their size.

        Parameters:
            other: The object to compare with the current instance.

        Returns:
            bool: True if the sizes of both objects are equal, False otherwise.
        """
        return self.size == other.size

    def __lt__(self, other):
        """
        Compare if the current object's size is < than another object's size.

        Parameters:
            other: The object to compare with the current instance.

        Returns:
            bool: True if the current object's size is less than
            the other object's size, False otherwise.
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compare if the current object's size is <= to another object's size.

        Parameters:
            other: The object to compare with the current instance.

        Returns:
            bool: True if the current object's size is less than
            or equal to the other object's size, False otherwise.
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
        Compare if the current object's size is > than another object's size.

        Parameters:
            other: The object to compare with the current instance.

        Returns:
            bool: True if the current object's size is greater
            than the other object's size, False otherwise.
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compare if the curr object's size is >= than to another object's size.

        Parameters:
            other: The object to compare with the current instance.

        Returns:
            bool: True if the current object's size is greater
            than or equal to the other object's size, False otherwise.
        """
        return self.size >= other.size
