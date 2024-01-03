#!/usr/bin/python3
"""
   A function defination in python using def
   We can also say
   if ord(ch) <= 97 and ord(ch) <= 122
   print(f"{ch}", end='')
   We can also add a call function i.e.
   uppercase(str)
   str = input("Enter your string: ")
"""

def uppercase(str):
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
