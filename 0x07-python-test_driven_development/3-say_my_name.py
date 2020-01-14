#!/usr/bin/python3
""" Function say_my_name """


def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first_name> <last_name>"

        Arguments:
                @first_name:
                            Must be a string otherwise a TypeError
                            is going to be printed.
                @last_name:
                            Must be a string otherwise a TypeError
                            is going to be printed.
                            Default value is empty
                            When a value is not given, is going to
                            be printed a space instead

        Return:
                Doesn't return anything, just print
                Prints in the stdout "My name is <first name> <last name>"
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
