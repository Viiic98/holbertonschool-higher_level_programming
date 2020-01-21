#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ is_same_class
        Check if type of an object is exactly a
        specific class
        Return:
                True if it is the same
                False if it is not the same
    """
    if type(obj) == a_class:
        return True
    else:
        return False
