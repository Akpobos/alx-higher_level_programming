#!/usr/bin/python3
"""Matrix Divided Module"""

def matrix_divided(matrix, div):
    """Functio that divides all elements of a matrix
    Args:
        matrix (list): The matrix
        div (int): The divisor

    Returns:
        A new matrix with all values divided by the divisor

    Raises:
        TypeError:
            matrix must be a matrix (list of lists) of integers/floats
            Each row of the matrix must have the same size
            div must be a number
        ZeroDivisionError:
            div can't be 0
    """
    if not isinstance(matrix, list) or not len(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    list_length = None

    for row in matrix:
        sub = []
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if list_length == None:
            list_length = len(row)
        if len(row) != list_length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            sub.append(round(i/div, 2))
        new_list.append(sub)
    return new_list
