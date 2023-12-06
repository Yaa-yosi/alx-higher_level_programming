#!/usr/bin/python3
def max_integer(my_list=[]):
    for num in my_list:
        if not my_list:
            return None
        elif num > my_list[0]:
            return num
