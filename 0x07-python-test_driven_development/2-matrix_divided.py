#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError ("div must be a number")
    if div == 0:
        raise TypeError ("division by zero")
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError ("Each row of the matrix must have the same size")
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]
