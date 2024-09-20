#!/usr/bin/python3
"""This module defines the 'Square' class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square instance.

        Parameters:
            size (int): The size of one side of the square.
                        Must be an integer >= 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size as an integer.
        """
        return self.__size  # Private attribute

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            Value (int):  The size of one side of the square.
                          Must be an integer >= 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # Private attribute

    @property
    def position(self):
        """
        Get the position at the coordinates.

        Returns:
            position (tuple): The position at the tuple's coordinates.
        """
        return self.__position  # private attribute

    @position.setter
    def position(self, value):
        """
        Set the position at the coordinates.

        Raises:
            TypeError: If 'position' is not a tuple.
                       if tuple has not 2 elements.
                       if 'position' has not 2 positives integers is not tuple.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = tuple(value)

    def area(self):
        """
        Compute the area of square.

        Returns:
            int: the result of side * side.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print in stdout the square with the character '#'.

        If the size is 0, print an empty line.

        If position[1] > 0, print 'position[1]' blank line(s)
        before printing the square.

        Print position[0] space before each row of square.

        Returns:
            None
        """
        print_list = []

        if self.__size == 0:
            return "\n"
        else:
            # Print blank line before
            if self.__position[1] > 0:
                print("\n" * (self.__position[1] - 1))

            for i in range(self.__size):
                # Insert space
                print_list.append(" " * self.__position[0] + "#" * self.__size)

        print("\n".join(print_list))

    def __str__(self):
        """
        Return a string representation of the square with the character '#'.

        If size is 0, returns an empty string with a newline.

        If `position[1] > 0`, the string starts with `position[1]` blank lines.

        Each row of the square contains `position[0]` spaces before
        the '#' characters to represent the horizontal offset.

        Returns:
            str: The string representation of the square,
            including any blank lines and spaces for the position.
        """
        print_list = []

        if self.__size == 0:
            return "\n"
        else:
            # Print blank line before
            if self.__position[1] > 0:
                print("" * (self.__position[1]))

            for i in range(self.__size):
                # Insert space
                print_list.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(print_list)
