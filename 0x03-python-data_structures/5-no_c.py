#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters C from  str"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))

