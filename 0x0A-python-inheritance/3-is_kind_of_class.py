#!/usr/bin/python3
"""Defining a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checker of  objects - it is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
