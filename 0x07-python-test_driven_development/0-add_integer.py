#!/bin/python3
#0-add_integer.py
"""definig a number if it is an integer"""
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b (both casted to integers if they are float).
        
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    # Checker of a and b if  both  integers or floats
    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Returnig the sum of a and b 
    return a + b

