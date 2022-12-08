#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elements in matrix:
        matri = list(map(lambda x: x**2, elements))
        new_matrix.append(matri)
    return(new_matrix)
