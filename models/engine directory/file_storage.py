"""
File Storage Module

This module provides a simple file-based storage mechanism using JSON.

Attributes:
    __file_path (str): Path to the JSON file.
    __objects (dict): Dictionary to store objects by class name and id.
"""

import json

class FileStorage:
    """
    Class representing a file-based storage mechanism using JSON.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store objects by class name and id.
    """

    def __init__(self, file_path):
        """
        Initializes the FileStorage instance.

        Args:
            file_path (str): Path to the JSON file.
        """
        self.__file_path = file_path
        self.__objects = {}

        # Load data from the file if it exists
        if self.file_exists():
            self.reload()

    def file_exists(self):
        """
        Check if the JSON file exists.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        try:
            with open(self.__file_path, 'r') as file:
                return True
        except FileNotFoundError:
            return False

    def all(self):
        """
        Returns the dictionary of objects.

        Returns:
            dict: Dictionary containing objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
            obj (dict): The object to add to the dictionary.

        Raises:
            ValueError: If obj is not a dictionary or has no 'id' key.
        """
        if not isinstance(obj, dict):
            raise ValueError("Object must be a dictionary")

        self.__objects[obj.__class__.name] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        with open(self.__file_path, 'r') as file:
            self.__objects = json.load(file)