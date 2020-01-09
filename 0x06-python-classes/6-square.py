#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
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
        return self.size * self.size

    def my_print(self):
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
