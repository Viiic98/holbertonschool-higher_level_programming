#!/usr/bin/python3
""" Module that add two numbers """


def add_integer(a, b=98):
    """ This function add two integers

        Arguments:
                @a:
                    Must be an integer or float, otherwise a
                    TypeError is going to be printed.
                    This argument a doesn't have a default value
                @b:
                    Must be an integer or float, otherwise a
                    TypeError is going to be printed.
                    The default value of this argument is 98
        Return:
                The result to add two numbers
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError('a must be an integer')
    else:
        a = round(a)
        a = int(a)
    if type(b) is not float and type(b) is not int:
        raise TypeError('b must be an integer')
    else:
        b = round(b)
        b = int(b)
    return a + b
