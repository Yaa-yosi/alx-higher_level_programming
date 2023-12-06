#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, member in enumerate(row):
            if idx == len(row) - 1:
                print("{:d}".format(member), end="")
            else:
                print("{:d}".format(member), end=" ")
        print()
