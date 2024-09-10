#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Return the key with the highest integer value in a dictionary.

    Parameters:
        a_dictionary (dict): A dictionary where keys are strings and values
                             are integers.
                             If the dictionary is empty or None, returns None.

    Returns:
        str or None: The key associated with the highest integer value.
                     If the dictionary is empty or None, returns None.
    """
    if a_dictionary is None:
        return None

    biggest_value = 0

    for key in a_dictionary:
        if a_dictionary[key] > biggest_value:
            biggest_value = a_dictionary[key]
            best_student = key

    return best_student
