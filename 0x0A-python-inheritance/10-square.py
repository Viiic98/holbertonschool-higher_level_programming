#!/usr/bin/python3
class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ Area method

            Raise an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ integer_validator

            Validate if value is an integer greater than 0
        """
        if type(value) is not int:
            raise TypeError('<name> must be an integer')
        elif value <= 0:
            raise ValueError('<name> must be greater than 0')
        else:
            return


class Rectangle(BaseGeometry):
    """ Subclass Rectangle """
    def __init__(self, width, height):
        """ Initialize object

            Arguments:
                    @self: Reference to itself
                    @width: Must be an integer greater than 0
                    @height: Must be an integer greater than 0
        """
        Rectangle.integer_validator(self, "", width)
        Rectangle.integer_validator(self, "", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Implement __str__ """
        w = self.__width
        h = self.__height
        return str("[{}] {:d}/{:d}".format(Rectangle.__name__, w, h))

    def area(self):
        """ Area method

            Return:
                    Area of a rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """ Subclass Square of Rectangle"""
    def __init__(self, size):
        """ Initialize object """
        self._Rectangle__width = size
        self._Rectangle__height = size
        self.integer_validator("", size)
        self.__size = size

    def area(self):
        """ Area method

            Return:
                    Area of a square
        """
        return self.__size * self.__size
