#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest int"""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for n in range(len(my_list)):
        if my_list[n] > big:
            big = my_list[n]

    return (big)


