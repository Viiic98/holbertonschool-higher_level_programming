#!/usr/bin/python3
class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ print_sorted
            Method that prints a sorted list of class
            Arguments:
                    @self: Reference to it self
            Return:
                    Print the values of MyList sorted
        """
        print(sorted(self))
