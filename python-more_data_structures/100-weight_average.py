#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Return the weighted average of all integers.

    Parameters:
        my_list (list): Contains tuples (<score>, <weigth>).

    Returns:
        average (float): ((1 * 2) + (2 * 1)
                         + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    """
    prod = 0
    dividend = 0
    divisor = 0
    for tup in my_list:
        # Mul each tuple to obtain a prod
        prod = tup[0] * tup[1]
        # Add each prod to obtain dividend and reset
        dividend += prod
        prod = 0
        # Add each weigth in the tuple
        divisor += tup[1]

    average = dividend / divisor

    return average
