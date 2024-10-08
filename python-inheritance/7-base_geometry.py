#!/usr/bin/python3
"""
This module defines a class 'BaseGeometry'.

The 'BaseGeometry' class itself serves as a base or abstract class for more
specific geometric shapes, such as rectangles or circles.
"""


class BaseGeometry:
    """
    Represent base geometry.

    Methods:
        area(self): Raises an exception indicating that the method is not yet
                    implemented and should be overridden by subclasses.

        integer_validator(self, name, value): Validates that a given value.
    """

    def area(self):
        """Raise an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value):
        """
        Validate that 'value' is a positive integer.

        Parameters:
            name (str):  The name of the value, we assume is always a string.
            value (int): The integer to validate.

        Raise:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is negative or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
