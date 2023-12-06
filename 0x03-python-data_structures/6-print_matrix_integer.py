#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for member in row:
            print("{:d}".format(member), end=" ")
        print()
