#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Parameters:
    roman_string (str): A string representing a Roman numeral. The string must
                        consist of valid Roman numeral characters ('I', 'V',
                        'X', 'L', 'C', 'D', 'M'). If the input is not a string
                        or if it's invalid, the function returns 0.

    Returns:
        int: The integer value corresponding to the Roman numeral, or 0 if
             the input is not a valid Roman numeral or is not a string."""
    if roman_to_int is None:
        return None
    # List to store arabic num style and roman key
    int_list = []
    key = ""

    # One dictonnary by decimal place
    thousands_dict = {"M": 1, "MM": 2, "MMM": 3}
    hundreds_dict = {
        "C": 1,
        "CC": 2,
        "CCC": 3,
        "CD": 4,
        "D": 5,
        "DC": 6,
        "DCC": 7,
        "DCCC": 6,
        "CM": 9,
    }
    tens_dict = {
        "X": 1,
        "XX": 2,
        "XXX": 3,
        "XL": 4,
        "L": 5,
        "LX": 6,
        "LXX": 7,
        "LXXX": 8,
        "XC": 9,
    }
    units_dict = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
    }

    # Search and get the thousands
    for char in roman_string:
        if char == "C" or char == "D":
            break
        if char == "M":
            key += "M"
    if key is not None:
        int_list.append(thousands_dict.get(key))
        key = ""

    # Search and get for the hundreds
    for char in roman_string:
        if char == "X" or char == "L":
            break
        if key is not None and key == "C" and char == "M":
            key += "M"
        elif char == "C":
            key += "C"
        elif char == "D":
            key += "D"
    if key is not None:
        int_list.append(hundreds_dict.get(key))
        key = ""

    # Search for tens
    for char in roman_string:
        if char == "I" or char == "V":
            break
        if key is not None and key == "X" and char == "C":
            key += "C"
        elif char == "X":
            key += "X"
        elif char == "L":
            key += "L"
    if key is not None:
        int_list.append(tens_dict.get(key))
        key = ""

    # Search for units
    for char in roman_string:
        if key is not None and key == "I" and char == "X":
            key += "X"
        elif char == "I":
            key += "I"
        elif char == "V":
            key += "V"
    if key is not None:
        int_list.append(units_dict.get(key))
        key = ""

    # Converts list into integer
    number = 0
    for digit in int_list:
        if digit is None and number == 0:
            continue
        elif number > 0 and digit is None:
            number *= 10
        else:
            number = number * 10 + digit

    return number
