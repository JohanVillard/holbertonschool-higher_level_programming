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
        self.__size = size  # Private attribute
        self.__position = position

    def area(self):
        """
        Compute the area of square.

        Returns:
            int: the result of side * side.
        """
        return self.__size * self.__size

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
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                # Print blank line before
                for i in range(self.position[1]):
                    print()

            for i in range(self.size):
                # Insert space
                for k in range(self.position[0]):
                    print(" ", end="")
                # Print square
                for j in range(self.size):
                    print("#", end="")
                print()

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
                       if 'position' has not 2 positives integers inot tuple.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers.")
        if not isinstance(tuple[0], int) or not isinstance(tuple[1]):
            raise TypeError("position must be a tuple of 2 positive integers.")

        self.__position = value
