#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = num * num
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix

#    new = []
#    for r in matrix:
#        for n in r:
#            re = n * n
#            new.append(re)
#    return new
