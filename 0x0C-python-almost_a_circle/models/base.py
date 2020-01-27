#!/usr/bin/python3
""" The base of all classes in this project """
import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Object to JSON """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Store object into a file """
        ljson = []
        filename = cls.__name__+".json"
        if list_objs is not None:
            for i in list_objs:
                ljson.append(cls.to_dictionary(i))
        else:
            ljson = []
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(ljson))

    @staticmethod
    def from_json_string(json_string):
        """ Read a file from JSON """
        my_l = []
        if json_string is None:
            return my_l
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns a instance with all attributes """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        filename = cls.__name__+".json"
        print(filename)
        try:
            with open(filename, 'r') as f:
                l = f.read()
        except:
            return []
