#!/usr/bin/python3
"""a class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initializing the new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a filtered dictionary."""
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    filtered_dict[attr] = self.__dict__[attr]
            return filtered_dict

    def reload_from_json(self, json):
        """Substitute all properties within a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
