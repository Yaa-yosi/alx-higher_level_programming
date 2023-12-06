#!/usr/bin/python3
def max_integer(my_list=[]):
    for num in my_list:
        if not my_list:
            return None
        elif num > my_list[0]:
            max_list = num
            return max_list
