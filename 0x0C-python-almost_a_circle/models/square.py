#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init method
            Initialize instances
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Str method defined

            What's going to happen when call the class
            with str or just print
        """
        s = "[Square] ("+str(self.id)+") "+str(self.x)
        s += "/"+str(self.y)+" - "+str(self.size)
        return s

    @property
    def size(self):
        """ Size's getter
            Return:
                    private Size
         """
        return self.width

    @size.setter
    def size(self, value):
        """ Size's setter
            Arguments:
                    @value: Must be and integer > 0
            Return:
                    Nothing, just set the value of Size
        """
        self.width = value
        self.height = value

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
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
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
        dic = {'id:': self.id, 'x': self.x,
               'size': self.size, 'y': self.y}
        return dic
