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
