#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5"""

def print_operation_result(operation, a, b):
    result = operation(a, b)
    print(f"{a} {operation.__name__} {b} = {result}")

def main():
    a = 10
    b = 5

    print_operation_result(add, a, b)
    print_operation_result(sub, a, b)
    print_operation_result(mul, a, b)
    print_operation_result(div, a, b)

