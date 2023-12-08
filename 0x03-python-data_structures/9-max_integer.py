#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    elif my_list:
        my_list.sort()
        new_list = my_list[::-1]
        return (new_list[0])
