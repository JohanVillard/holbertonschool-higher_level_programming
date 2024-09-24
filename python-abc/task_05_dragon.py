#!/usr/bin/python3
"""This module defines a 'Dragon' class."""


class SwimMixin:
    """Represent the action of swim."""

    def swim(self):
        """
        Simulate the creature swimming.

        This method prints a message indicating that the creature is swimming.
        It represents the action of the creature in its environment.
        """
        print("The creature swims!")


class FlyMixin:
    """Represent the action of fly."""

    def fly(self):
        """
        Simulate the creature flying.

        This method prints a message indicating that the creature is flying.
        It represents the action of the creature in its environment.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""

    def roar(self):
        """
        Simulate the dragon roaring.

        This method prints a message indicating that the dragon is roaring.
        It represents the action of the roaring in its environment.
        """
        print("The dragon roars!")
