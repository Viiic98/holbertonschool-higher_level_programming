#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ inherits_from
        Check if obj is a sub class of a_class

        Return:
                True if it is a subclass
                False if it is not a subclass
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
