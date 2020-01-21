#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ is_kind_of_class
        Check if obj is an instance of a_class
        Return:
                True if it is an instance
                False if it is not an instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
