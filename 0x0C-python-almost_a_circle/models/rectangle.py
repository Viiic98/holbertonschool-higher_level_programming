#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width's getter
            Return:
                    private width
         """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width's setter
            Arguments:
                    @value: Must be and integer > 0
            Return:
                    Nothing, just set the value of width
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Height's getter
            Return:
                    private height
         """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height's setter
            Arguments:
                    @value: Must be and integer > 0
            Return:
                    Nothing, just set the value of Height
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ X's getter
            Return:
                    private X
         """
        return self.__x

    @x.setter
    def x(self, value):
        """ X's setter
            Arguments:
                    @value: Must be and integer > 0
            Return:
                    Nothing, just set the value of X
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ Y's getter
            Return:
                    private Y
         """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y's setter
            Arguments:
                    @value: Must be and integer > 0
            Return:
                    Nothing, just set the value of Y
        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ Method that find the rectangle's area
            Return:
                    Rectangle's area
        """
        return self.width * self.height

    def display(self):
        """ Method that displays a rectangle
            Return:
                    Print in stdout a rectangle
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            for k in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Str method defined

            What's going to happen when call the class
            with str or just print
        """
        s = "[Rectangle] ("+str(self.id)+") "+str(self.x)+"/"+str(self.y)
        s += " - "+str(self.width)+"/"+str(self.height)
        return s

    def update(self, *args, **kwargs):
        """ Method that update the information of a rectangle

            Arguments:
                    @args: aguments
                    @kwargs: specific keys and it's value
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                else:
                    return
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary method
            Return:
                    a dictionary that show every key and value
        """
        dic = {'x': self.__x, 'y': self.__y, 'id': self.id,
               'height': self.__height, 'width': self.__width}
        return dic
