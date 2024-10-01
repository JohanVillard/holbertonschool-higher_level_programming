"""This module serialize and deserialise custom Python object using pickle."""

import pickle


class CustomObject:
    """Represent a custom object."""

    def __init__(self, name, age, is_student):
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
        for key, value in self.__dict__.items():
            print(f"{key.title().replace("_", " ")}: {value}")

    def serialize(self, filename):
        """
        Serialize the current instance of the CustomObject.

        Parameter:
            filename (str): Name of the file which the data is stored.

        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of the CustomObject.

        Parameter:
            filename (str): The name of the file which contains the data to
                            process.
        Returns:
            obj: The function return an loaded instance of the CustomObject.
        """
        with open(filename, "rb") as f:
            return pickle.load(f)
