#!/usr/bin/python3
def print_square(size):
    """ Function that prints a square

        Arguments:
                @size:
                    Is the length of the square.
                    Must be an integer or float greater than 0, otherwise
                    a TypeError is going to be raised.
                    Size can't be less than zero, otherwise a ValueError
                    is going to be raised.
                    If is float and less than 0, a Type error is going
                    to be raised.

        Return:
                Doesn't have return.
                Print a square in the stdout.
    """
    if type(size) is float or type(size) is int:
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            size = int(size)
    else:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
