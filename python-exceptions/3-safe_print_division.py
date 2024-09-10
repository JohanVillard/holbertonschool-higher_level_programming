#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Parameters:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float or None: The result of the division if successful,
                       or None if there is a division by zero.

    Side effect:
        Prints the result of the division inside the `finally` block.
        If the division is successful, it prints the result formatted
        to one decimal place. If there is a ZeroDivisionError,
        it prints 'None'.
    """
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        if quotient is not None:
            print("Inside result: {:.1f}".format(quotient))
        else:
            print("Inside result: {}".format(quotient))

    return quotient
