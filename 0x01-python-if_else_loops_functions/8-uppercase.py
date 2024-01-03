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

def uppercase(str): """Convert str from uppercase to lowercase"""
    for i in str: """Look at chr in str and modify them individually"""
        if ord("a") <= ord(i) <= ord("z"): """Check ASCII values using ord()"""
            i = chr(ord(i) - 32) """Convert them into UPPERCASE"""
        print("{:s}".format(i), end="") """Print the result"""
    print()
