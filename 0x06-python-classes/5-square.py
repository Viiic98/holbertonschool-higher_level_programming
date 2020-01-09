#!/usr/bin/python3
""" Square """


class Square:
    """ Define Square Class """
    def __init__(self, size=0):
        """ Initialize Atributtes
        Args:
            Size: Must be an integer greater than 0
        """
        self.__size = size

    @property
    def size(self):
        """ Getter of size
        Return:
              Value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of size
        Args:
            value: Must be an integer and greater than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Area
        Args:
            None
        Return:
             Square of size
        """
        return self.__size * self.__size

    def my_print(self):
        """ Print
        Args:
            None
        Return:
             Print a square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
