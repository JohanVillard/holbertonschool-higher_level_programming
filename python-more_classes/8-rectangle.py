#!/usr/bin/python3
"""This module defines a 'Rectangle' class."""


class Rectangle:
    """
    Represents a rectangle shape defined by its width and height.

    The class allows setting and getting the width and height of the rectangle,
    with validation to ensure both are integers and non-negative.
    """

    # Class attributes
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

    # Width getter-setter
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

    # Height getter-setter
    @property
    def height(self):
        """
        Get the value of the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

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

    def area(self):
        """
        Compute the area of te rectangle.

        Returns:
            int: The current area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        If 'width' or 'height' are equal to 0, perimeter equel 0.

        Returns:
            int: The current perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Print the rectangle with the character "print_symbol".

        If 'width' or 'height' is equal to 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""

        for i in range(self.height):
            for j in range(self.width):
                print("{}".format(self.print_symbol), end="")

            if i < self.height - 1:
                print()

        return str()

    def __repr__(self):
        """
        Print a representation of the rectangle.

        Returns:
            ....
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete an instance of rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare the area of two rectangles.

        Return the one with the greater or equal area.

        Parameters:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater or equal area.
                       If both have the same area, rect_1 is returned.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance
                       of the Rectangle class.
        """
        # Check if the parameters are instance of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # Compute the areas of the 2 rectangles
        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()

        # Compare the 2 areas and return
        if rect_1_area >= rect_2_area:
            return rect_1

        return rect_2
