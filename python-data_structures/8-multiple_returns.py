#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Parameters:
    sentence (str): A string whose length and first character will be returned.

    Returns:
    tuple: A tuple containing:
        - The length of the string (int).
        - The first character of the string (str) if the string is not empty.
          If the string is empty, returns None as the first character.
    """
    if len(sentence) == 0:
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
