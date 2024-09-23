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
