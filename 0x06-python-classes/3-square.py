#!/usr/bin/python3
""" Square """


class Square:
    """ Define Square class """
    def __init__(self, size=0):
        """ Initialize Atributtes
        Args:
            Size: Must be an integer greater than 0
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """ Area
        Args:
            None
        Return:
            Square of size
        """
        size = self.__size
        return size * size
