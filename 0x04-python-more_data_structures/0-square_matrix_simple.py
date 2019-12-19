#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list(map(list, matrix))
    a = 0
    for i in new:
        b = 0
        for j in i:
            new[a][b] = j * j
            b += 1
        a += 1
    return new
