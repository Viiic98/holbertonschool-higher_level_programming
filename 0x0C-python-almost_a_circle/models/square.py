#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        s = "[Square] ("+str(self.id)+") "+str(self.x)
        s += "/"+str(self.y)+" - "+str(self.size)
        return s

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
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
        dic = {'id:': self.id, 'x': self.x,
               'size': self.size, 'y': self.y}
        return dic
