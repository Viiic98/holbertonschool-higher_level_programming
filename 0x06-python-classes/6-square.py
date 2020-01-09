#!/usr/bin/python3
""" Square """


class Square:
    """ Define Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize Atributtes
        Args:
            Size: Must be an integer greater than 0
            Position: Must be a tuple, integer and greater\
                      than 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter position
        Args:
            None
        Return:
             The position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter of position
        Args:
            value: Must be a tuple, integer and\
                   greater than 0y
        """
        err = "position must be a tuple of 2 positive integers"
        if len(value) == 2 and type(value) == tuple:
            if type(value[0]) == int and type(value[1]) == int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError(err)
            else:
                raise TypeError(err)
        else:
            raise TypeError(err)

    def area(self):
        """ Area
        Args:
            None
        Return:
             Square of size
        """
        return self.size * self.size

    def my_print(self):
        """ Print
        Args:
            None
        Return:
             Print a square
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for j in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for l in range(self.size):
                    print("#", end="")
                print("")
