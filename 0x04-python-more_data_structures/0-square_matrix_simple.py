#!?usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map((lambda x: x ** 2), x)) for x in matrix]
    return new_matrix
