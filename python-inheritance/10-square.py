#!/usr/bin/python3
"""This module defines a class 'BaseGeometry'."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a new Square instance with the same width and height.

        This constructor validates that 'size' is a positive integer
        using the 'integer_validator' method inherited from BaseGeometry.

        Parameters:
            size (int): The size of the square, must be private and
                        must be positive integer.
        """
        super().integer_validator("size", size)
        super().__init__(width=size, height=size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size**2
