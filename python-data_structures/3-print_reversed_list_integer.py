#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list, in reverse order.

    Description:
        This function prints a reverse list of all integers.
        The format is one integer by line.

    Parameters:
        my_list(list): to reverse.

    Returns:
        None.
    """
    for number in my_list[::-1]:
        print(number)
