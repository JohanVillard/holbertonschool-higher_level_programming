#!/usr/bin/python3
"""This module defines a 'Shapes' class and its sub-class."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Represent an abstract geometrical shape class.

    This class serves as a base for all shape subclasses and
    requires the implementation of area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Compute the area of a shape.

        Return:
            The value of the shape's area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of a shape.

        Return:
            The value of the shape's perimeter.
        """
        pass


class Circle(Shape):
    """Represent a circle, a subclass of Shape."""

    def __init__(self, radius):
        """
        Initialize an instance of Circle.

        Parameters:
            radius (int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of a circle.

        Returns:
            float: The value of the area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Return the perimeter of a circle.

        Returns:
            float: The value of the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectancle, a subclass of Shape."""

    def __init__(self, width, height):
        """
        Initialize an in instance of Rectangle.

        Parameters:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of a rectangle.

        Returns:
            int: The value of the area of a rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        Returns:
            float: The value of the perimeter of a rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(objs):
    """
    Print area and perimeter of all subclass of shape.

    Parameters:
        obj (Shape): An instance of a Shape subclass.
    """
    for shape in objs:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    shapes = [Circle(3), Rectangle(5, 4)]

    shape_info(shapes)
