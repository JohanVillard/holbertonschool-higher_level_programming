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
            TypeError: If 'value' is not an integer or is a bool, raises a
                       TypeError with the message '<name> must be an integer'.
            ValueError: If 'value' is negative or equal to 0, raises a
                        'ValueError' with the message '<name> must be greater
                        than 0'."
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance with width and height.

        The constructor validates that the width and height are positive
        integers using the 'integer_validator' method inherited from
        BaseGeometry.

        Parameters:
            width (int): The width of the rectangle, must be a positive
                         integer.
            height (int): The height of the rectangle, must be a positive
                          integer.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
