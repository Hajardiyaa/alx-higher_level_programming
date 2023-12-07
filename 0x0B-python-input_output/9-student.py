#!/usr/bin/python3
"""Contains the clas "Student"""
class Student:
    """student's id"""
    def __init__(self, first_name, last_name, age):
        """Initializing the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the student's instance dictionary """
        return self.__dict__
