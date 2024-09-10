#!/usr/bin/python3


def raise_exception():
    """
    Raise a TypeError exception.

    Description:
        This function raises a TypeError when a condition is met.
        In this case, the condition checks if `x` is not of type `str`.

    Raises:
    TypeError: Always raised because `x` (an integer)
               is compared with `str`'s type.
    """
    x = 1
    if x is not type(str):
        raise TypeError()
