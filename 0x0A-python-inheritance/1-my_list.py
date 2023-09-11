#!/usr/bin/python3
"""Defiing an inherited list class MyList."""


class MyList(list):
    """Implementing a sort print for the built-in list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
