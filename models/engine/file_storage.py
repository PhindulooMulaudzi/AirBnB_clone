#!/usr/bin/python3

"""
File Storage Module - A simple file-based storage mechanism using JSON.

This module defines the FileStorage class, which implements a simple
file-based storage mechanism using JSON. It provides methods to interact
with the stored objects.

Attributes:
    __file_path (str): Path to the JSON file.
    __objects (dict): Dictionary to store objects by class name and id.
"""

import json
from os.path import exists


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
        Return the dictionary of objects.

        Returns:
            dict: Dictionary containing objects.
        """
        cls.reload()
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """
        Add a new object to the dictionary of objects.

        Args:
            obj (BaseModel): The object to add to the dictionary.
        """
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        cls.__objects[key] = obj.__dict__

    @classmethod
    def save(cls):
        """Serialize __objects to the JSON file."""
        with open(cls.__file_path, 'w') as file:
            json.dump(cls.__objects, file, indent=4,
                      sort_keys=True, default=str)

    @classmethod
    def reload(cls):
        """Deserialize the JSON file to __objects."""
        if not exists(cls.__file_path):
            # Create the file if it doesn't exist
            with open(cls.__file_path, 'w') as file:
                file.write(json.dumps({}))  # Write an empty JSON object

        # Load the JSON data into __objects
        with open(cls.__file_path, 'r') as file:
            cls.__objects = json.load(file)
