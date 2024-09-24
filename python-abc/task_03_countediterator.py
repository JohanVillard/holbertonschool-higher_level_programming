#!/usr/bin/python3
"""This module defines a 'CountedIterator' class."""


class CountedIterator:
    """Represent a custom iterator that tracks the number of iterations."""

    def __init__(self, some_iterable):
        """
        Initialize the CountedIterator.

        Parameters:
            some_iterable (iterable): The iterable object to wrap with the
                                      counter.

        Attributes:
            iterator (iterator): The underlying iterator created from the
                                 iterable.
            count (int): Tracks how many elements have been iterated over.
            size (int): The total size of the iterable (number of elements).
        """
        self.iterator = iter(some_iterable)
        self.count = 0
        self.size = len(some_iterable)

    def get_count(self):
        """
        Get the current iteration count.

        Returns:
            int: The number of elements iterated over so far.
        """
        return self.count

    def __next__(self):
        """
        Get the next item from the iterator, increasing the count.

        Raises:
            StopIteration: If the number of iterations exceeds the size of
                           the iterable.

        Returns:
            object: The next item from the iterable.
        """
        if self.count <= self.size:
            self.count += 1
            next_iter = next(self.iterator)
            return next_iter
        else:
            raise StopIteration
