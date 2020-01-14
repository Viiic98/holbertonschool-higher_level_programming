#!/usr/bin/python3
""" Function """


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix

        Arguments:
                @matrix:
                        Must be a list of integers or floats otherwise a
                        TypeError is going to be printed.
                        Each row must be of the same size other wise a
                        TypeError is going to be printed
                @div:
                        Must be an integer or float, otherwise a TypeError
                        is going to be printed
                        The value of div can't be 0, otherwise a ZeroDivisionError
                        is going to be printed

        Return:
                A new matrix divided by div rounded to 2 decimal places
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) is not float and type(div) is not int:
        raise TypeError('div must be a number')
    else:
        x = len(matrix)
        if x == 0:
            raise TypeError('Each row of the matrix must have the same size')
        else:
            y = len(matrix[0])
            new_m = [[0 for i in range(y)] for j in range(x)]
            for i in range(len(matrix)):
                if len(matrix[i]) is not y:
                    raise TypeError('Each row of the matrix must have the same size')
                else:
                    for j in range(len(matrix[i])):
                        if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
                        else:
                            new_m[i][j] = round(matrix[i][j] / div, 2)
        return new_m
