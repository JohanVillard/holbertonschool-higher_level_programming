#!/usr/bin/python3
"""This module defines a class 'BaseGeometry'."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """
        Raise an exception indicating the method is not implemented.

        This method is meant to be overridden by subclasses to calculate
        the area of a shape.

        Raise:
            Exception: Always raises an Exception with the message
                       'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.

        Parameters:
            name (str):  The name of the value, we assume is always a string.
            value (int): The integer to validate.

        Raise:
            TypeError: If 'value' is not an integer, raises a ValueError with
                       the message '<name> must be an integer'.
            ValueError: If 'value' is negative or equal to 0, raises a
                        'ValueError' with the message '<name> must be greater
                        than 0'."
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
