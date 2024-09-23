#!/usr/bin/python3
"""This module defines an 'Animal' class and its Subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Represent an abstract animal class.

    This class serves as a base for all animal subclasses and
    requires the implementation of the sound method.
    """

    @abstractmethod
    def sound(self):
        """
        Return the sound that the animal makes.

        This method must be overridden by subclasses.

        Returns:
            str: The sound produced by the animal.
        """
        pass


class Dog(Animal):
    """Represent a dog, a subclass of Animal."""

    def sound(self):
        """
        Return the sound of a dog.

        Returns:
            str: The sound produced by the dog (e.g., "Bark").
        """
        return "Bark"


class Cat(Animal):
    """Represent a cat, a subclass of Animal."""

    def sound(self):
        """
        Return the sound of a cat.

        Returns:
            str: The sound produced by the cat (e.g., "Meow").
        """
        return "Meow"
