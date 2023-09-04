#!/bin/python3
#2-matrix_divided.py
"""dividing all elements of a matrix"""
def matrix_divided(matrix, div):
    """
    Args:
        matrix (list of lists): it contains integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If division is not a number (int or float).
        ZeroDivisionError: If division is equal to 0.
    """
    # Checker of the matrix if it is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Checker of all rows of the matrix 
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Checker if divisor is (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Checker if divisor is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix 
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix

