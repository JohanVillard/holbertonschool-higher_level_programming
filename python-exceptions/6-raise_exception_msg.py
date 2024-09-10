#!/usr/bin/python3


def raise_exception_msg(message=""):
    """
    Raises a NameError exception with a custom message.

    Parameters:
    message (str): The message to be passed with the NameError.
                   Default is an empty string.

    Raises:
    NameError: Always raised, and includes the provided message.
    """
    x = 1

    if x is not type(str):
        raise NameError(message)
