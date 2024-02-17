#!/usr/bin/python3
""" fct that inserts a line of text to a file, after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line"""

    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
