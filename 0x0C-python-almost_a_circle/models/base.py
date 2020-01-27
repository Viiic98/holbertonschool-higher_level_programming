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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ljson = []
        filename = cls.__name__+".json"
        for i in list_objs:
            dir = cls.to_dictionary(i)
            ljson.append(cls.to_json_string(dir))
        with open(filename, mode='w', encoding="UTF-8") as f:
            json.dump(ljson, f)

    @staticmethod
    def from_json_string(json_string):
        my_l = []
        if json_string is None:
            return my_l
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = Square(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__+".json"
        print(filename)
        try:
            with open(filename, 'r') as f:
                l = f.read()
                print(type(l))
        except:
            print("empty file")
            return []
