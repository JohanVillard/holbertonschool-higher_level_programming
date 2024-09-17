#!/usr/bin/python3
"""This module defines a 'Rectangle' class."""


class Rectangle:
    """
    Represents a rectangle shape defined by its width and height.

    The class allows setting and getting the width and height of the rectangle,
    with validation to ensure both are integers and non-negative.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle instance with a given width and height.

        Parameters:
            width (int): The width of the rectangle.
                         It must be a non-negative integer.
            height (int): The height of the rectangle.
                          It must be a non-negative integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Get the value of the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the width of the rectangle.

        Parameters:
            value (int): The new width of the rectangle.
                         It must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the value of the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Set the value of the height of the rectangle.

        Parameters:
            value (int): The new height of the rectangle.
                         It must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
