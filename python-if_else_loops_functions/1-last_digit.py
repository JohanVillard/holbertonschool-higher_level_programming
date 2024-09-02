#!/usr/bin/python3
"""
Calculates the last digit, and prints a message.

Indicating whether the last digit is greater than 5,
is 0, or is less than 6 and not 0.
"""

import random

number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (number * -1) % 10
    last_digit *= -1
else:
    last_digit = number % 10

if last_digit > 5:
    end_of_str = " and is greater than 5"
elif last_digit == 0:
    end_of_str = " and is 0"
elif last_digit < 6 and last_digit != 0:
    end_of_str = " and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit}{end_of_str}")
