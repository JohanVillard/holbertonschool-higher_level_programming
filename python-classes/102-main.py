#!/usr/bin/python3
Square = __import__("102-square").Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

s_8 = Square(8)
s_6 = Square(6)

if s_8 < s_6:
    print("Square 8 < Square 6")
if s_8 <= s_6:
    print("Square 8 <= Square 6")
if s_8 == s_6:
    print("Square 8 == Square 6")
if s_8 != s_6:
    print("Square 8 != Square 6")
if s_8 > s_6:
    print("Square 8 > Square 6")
if s_8 >= s_6:
    print("Square 8 >= Square 6")
