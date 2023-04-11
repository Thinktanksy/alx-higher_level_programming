#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Function to check if object is an instance of specified class.
    
    Args:
    obj (object): Object to check
    a_class (class): Class to check against
    
    Returns:
    bool: True if object is an instance of specified class, False otherwise.
    """
    return isinstance(obj, a_class)
