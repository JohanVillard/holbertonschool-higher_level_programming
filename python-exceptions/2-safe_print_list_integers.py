#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first 'x' elements of a list and only integers.

    Parameters:
        my_list (list): A list that can contain elements
                        of any type (integers, strings, etc.).
        x (int): The number of elements to access in my_list.
                 If x is greater than the length of my_list,
                 the function will attempt to access only
                 the available elements without raising an IndexError.

    Returns:
        int: The number of integers successfully printed.
    """
    count = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            count += 1
            if x == count:
                break
        except TypeError:
            pass
        except ValueError:
            pass

    print()

    return count
