#!/usr/bin/python3
"""This module provides a 'FlyingFish' class."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """
        Simulate the fish swimming.

        This method prints a message indicating that the fish is swimming.
        It represents the action of the fish in its environment.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Describe the habitat of the fish.

        This method prints a message indicating that the fish lives in water.
        It is a simple description of the fish's natural environment.
        """
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """
        Simulate the bird flying.

        This method prints a message indicating that the bird is flying.
        It represents the action of the bird in its environment.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Describe the habitat of the bird.

        This method prints a message indicating that the bird lives in the sky.
        It is a simple description of the bird's natural environment.
        """
        print("The bird lives in sky")


class FlyingFish(Bird, Fish):
    """Represent a flying fish that inherits from 'Fish' and 'Bird' class."""

    def swim(self):
        """
        Simulate the flying fish swimming.

        This method prints a message indicating that the flying fish is
        swimming. It represents the action of the flying fish in its
        environment.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Simulate the flying fish soaring.

        This method prints a message indicating that the bird is soaring.
        It represents the action of the flying fish in its environment.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Describe the habitat of the flying fish.

        This method prints a message indicating that the fish lives in water
        and the sky. It is a simple description of the flying fish's natural
        environment.
        """
        print("The flying fish lives both in water and the sky!")
