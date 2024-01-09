#!/bin/usr/python3
""" function to read a file"""
def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as new:
            print(new.read(), end="")
