#!/usr/bin/python3
"""This module defines a class 'BaseGeometry'."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
