#!/usr/bin/python3
"""
Classifies random numbers as either negative, zero, or positive.

It uses the `random` module to generate the number and then uses
conditional statements to check whether the number is less than zero,
equal to zero, or greater than zero. The result is printed to the console.
"""

import random

number = random.randint(-10, 10)
if number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is positive")
