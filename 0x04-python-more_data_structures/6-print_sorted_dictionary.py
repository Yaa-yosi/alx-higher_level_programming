#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)
    for key in new:
        print(f"{key}: {a_dictionary[key]}")
