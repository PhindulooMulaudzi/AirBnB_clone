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

    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """
        Returns the dictionary of objects.

        Returns:
            dict: Dictionary containing objects.
        """
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
            obj (BaseModel): The object to add to the dictionary.
        """
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        cls.__objects[key] = obj.__dict__

    @classmethod
    def save(cls):
        """
        Serializes __objects to the JSON file.
        """
        with open(cls.__file_path, 'w') as file:
            json.dump(cls.__objects, file, indent=4)

    @classmethod
    def reload(cls):
        """
        Deserializes the JSON file to __objects.
        """
        with open(cls.__file_path, 'r') as file:
            cls.__objects = json.load(file)
