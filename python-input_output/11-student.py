#!/usr/bin/python3
"""This module defines a 'Student' class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize an instance of Student.

        Parameters:
            first_name (str): The first_name of the student.
            last_name (str): The last_name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Parameter:
            attrs (list): The list that contains the attributes which are
                          displayed. None by default.

        Returns:
            dict: Returns a dictionary which contains attributes set in attrs.
                  If attrs is empty, returns all attributes.
        """
        # Check if attrs is empty
        if attrs:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Parameter:
            json (dict): The dictionary where the new attributes are stored.
        """
        for key, value in json.items():
            setattr(self, key, value)
