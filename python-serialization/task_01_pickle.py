"""This module serialize and deserialise custom Python object using pickle."""

import os
import pickle


class CustomObject:
    """Represent a custom object."""

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a custom object.

        Parameters:
            name (str): The name of the CustomObject.
            age (int): The age of the CustomObject.
            is_student (bool): True if the CustomObject is a student.
                               False if not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the instance's attribute of the CustomObject."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the CustomObject.

        Parameter:
            filename (str): Name of the file which the data is stored.

        Returns:
            If an error occurs, return None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of the CustomObject.

        Parameter:
            filename (str): The name of the file which contains the data to
                            process.
        Returns:
            obj: The function return an loaded instance of the CustomObject.
                 If an error occurs, return None
        """
        # Check if file exists
        if not os.path.exists(filename):
            return None

        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
