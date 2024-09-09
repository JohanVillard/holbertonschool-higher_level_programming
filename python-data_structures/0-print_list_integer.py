#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    Print all integers of a list.

    Description:
        This function prints all integers of a list.
        One integer by line. We assume that the list conains only integers.

    Parameters:
        my_list:
            is a list of integer to print.

    Return:
        None
    """
    for integer in my_list:
        print("{:d}".format(integer))
