#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    transposed = []
    for row in matrix:
        transposed.append([i**2 for i in row])
    return transposed
