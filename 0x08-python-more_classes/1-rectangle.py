#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initialize object, attributes

            Arguments:
                    @self:
                            Reference to itself attributes
                    @width:
                            Must be an integer, otherwise a TypeError
                            is going to be raised
                            Must be >= 0, otherwise a ValueError is
                            going to be raised
                    @height:
                            Must be an integer, otherwise a TypeError
                            is going to be raised
                            Must be >= 0, otherwise a ValueError is
                            going to be raised
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Property of attribute width

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    The attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of the width attribute

            Arguments:
                    @self:
                            Reference to itself attributes
                    @value:
                            Must be an integer, otherwise a TypeError
                            is going to be raised
                            Must be >= 0, otherwise a ValueError is
                            going to be raised

            Return:
                    Nothing, just set the value of width
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Property of attribute height

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    The attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of the height attribute

            Arguments:
                    @self:
                            Reference to itself attributes
                    @value:
                            Must be an integer, otherwise a TypeError
                            is going to be raised
                            Must be >= 0, otherwise a ValueError is
                            going to be raised

            Return:
                    Nothing, just set the value of height
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
