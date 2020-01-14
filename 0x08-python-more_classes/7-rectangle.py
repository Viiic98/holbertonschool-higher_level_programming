#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

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
        self.__number = self.m_number()

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

    def area(self):
        """ Method that calculates the area

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    Area of a rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the perimeter

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    Perimeter of rectangle or 0 when the value
                    of width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ Set the return for "__str__"

            When __str__ or print are called is going to print
            a specific thing

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    String that contain the rectangle
        """
        s = ""
        if self.width == 0 or self.height == 0:
            return s
        else:
            for i in range(self.height):
                for j in range(self.width):
                    s += str(self.print_symbol)
                if i + 1 != self.height:
                    s += "\n"
            return s

    def __repr__(self):
        """ __repr__ method

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    Returns a string with the name of class and
                    value of width and height
        """
        return "Rectangle ("+ str(self.width) + ", "+ str(self.height) + ")"

    def __del__(self):
        """ Configure the "__del__" method

            What is going to happen when __del__ is called

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    Nothing, only decrease number of instances and print a
                    message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def number(self):
        """ Property of attribute number

            Arguments:
                    @self:
                            Reference to itself attributes

            Return:
                    The attribute number
        """
        return self.number

    @classmethod
    def m_number(cls):
        """ Class method that count the number of instances

            Arguments:
                    @cls:
                            Is the reference to class

            Return:
                    The value of number of instances increased
        """
        Rectangle.number_of_instances += 1
        return Rectangle.number_of_instances
