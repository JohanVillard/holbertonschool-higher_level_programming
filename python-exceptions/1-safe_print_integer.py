#!/usr/bin/python3


def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().

    Parameters:
        value (any type): The value to print. It will be printed
        if it can be formatted as an integer.
    Returns:
        bool: True if value is successfully printed as an integer,
        otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        pass

    return False
