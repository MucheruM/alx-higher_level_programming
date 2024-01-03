#!/usr/bin/python3
"""
A function definition that prints the last digit of a num
"""


def print_last_digit(number):
    if number < 0:
        last_num = (-number % 10)
    elif number >= 0:
        last_num = number % 10
    print("{last_num}", end="")
    return last_num
