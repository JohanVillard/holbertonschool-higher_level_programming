#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divide elements from two lists element-wise and handles exceptions.

    Parameters:
        my_list_1 (list): The 1st list, which can contain elements of any type
                          (integers, strings, etc.).
        my_list_2 (list): The 2nd list, which can contain elements of any type
                          (integers, strings, etc.).
        list_length (int): The number of elements to divide.
                           This can be larger than the length of either list.

    Returns:
        list: A new list containing the results of the divisions.
              If an element cannot be divided due to a ZeroDivisionError,
              TypeError, or IndexError, the result for that division will be 0.

    Exceptions handled:
    - TypeError: If an element in either list is not a number,
                 the division result will be 0, and "wrong type" is printed.
    - ZeroDivisionError: If division by zero is attempted,
                         the result will be 0, and "division by 0" is printed.
    - IndexError: If the index is out of range for either list,
                  the result will be 0, and "out of range" is printed.
    """
    new_list = []
    quotient = 0
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            quotient = 0
            print("wrong type")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            new_list.append(quotient)

    return new_list
