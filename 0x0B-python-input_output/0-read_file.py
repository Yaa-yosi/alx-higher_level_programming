#!/bin/usr/python3

def read_file(filename=""):
    with open("my_file_0.txt", encoding="UTF8") as new:
        new1 = new.read()
        print(new1)
