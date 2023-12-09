#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_weight = 0
        weighted_sum = 0
        for pair in my_list:
            weighted_sum += pair[0] * pair[1]
            total_weight += pair[1]
        return weighted_sum / total_weight if total_weight != 0 else 0
    else:
        return 0
