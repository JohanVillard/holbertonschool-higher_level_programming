#!/usr/bin/python3
"""
This module defines a 'Rectangle' class.

The Rectangle class represent a geometric rectangle and allows for the
manipulation of its dimansions (with and height). It provides functionality
for calculating the rectangle's area, perimter, and displaying the rectangle
as a string. Additionaly, it offers comparison between two rectangle instances
based on their areas and a factory method for creating squared-shaped
rectangles.

Attributes:
    number_of_instances (int): A class attribute that keeps track of the number
                               of active Rectangle instances.
    print_symbol (any): A class attribute that defines the symbol used for
                        string representation of the rectangle.
                        The default symbol is '#'.
"""


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
        Compute the area of the rectangle.

        Returns:
            int: The current area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        If 'width' or 'height' are equal to 0, perimeter equal 0.

        Returns:
            int: The current perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rect using the 'print_symbol'.

        The rectangle is drawn using the 'print_symbol' attribute. If 'width'
        or 'height' is equal to 0, an empty string is returned.

        Returns:
            str: A string representation of the rectangle using 'print_symbol',
                 or an empty string if the rectangle has no area.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol_list = []
        for i in range(self.__height):
            symbol_list.append(self.__width * self.print_symbol)

        return "\n".join(symbol_list)

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance.

         This method is used to provide an unambiguous string representation
         of the rectangle, typically for debugging or logging purposes. It
         returns a string that can be used to recreate the rectangle object
         with the same width and height.

         Returns:
             str: A string in the format 'Rectangle(width, height)', where
             'width' and 'height' are the dimensions of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Handle the deletion of a Rectangle instance.

        This method is called when the instance is about to be destroyed.
        It decreases the class variable `number_of_instances` by one and
        prints a farewell message to the console.

        Side Effects:
            - Decrements the `Rectangle.number_of_instances` class variable.
            - Prints a message 'Bye rectangle...' to indicate that the
            object is being deleted.
        """
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

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with equal width and height.

        This is a factory method that returns a Rectangle instance where
        both the 'width' and 'height' are set to the provided 'size' value.

        Parameters:
            size (int, optional): The size for both the width and height of the
                                  rectangle. Defaults to 0.

        Returns:
            Rectangle: A new instance of the Rectangle class with equal
                       width and height.
        """
        return cls(height=size, width=size)
