#!/usr/bin/env python3

from datetime import datetime
from uuid import uuid4

class BaseModel:
    """
    Base class for models in the AirBnB clone project.

    Public Instance Attributes:
    - id (str): Unique identifier for each instance.
    - created_at (datetime): Date and time when the instance was created.
    - updated_at (datetime): Date and time when the instance was last updated.

    Public Class Attributes:
    - my_number (int): Total count of instances created.

    Public Instance Methods:
    - save(): Updates the 'updated_at' attribute with the current datetime.
    - to_dict(): Returns a dictionary containing instance attributes in a specified format.
    - __str__(): Returns a string representation of the instance.

    """
    my_number = 0

    def __init__(self):
        """
        Initializes a BaseModel instance with a unique 'id', creation time,
        and updates the 'my_number' count.

        """
        self.id = uuid4()

        current_time = datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

        BaseModel.my_number += 1

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts instance attributes to a dictionary format.

        """
        instance_dict = self.__dict__.copy()

        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        """
        class_name = self.__class__.__name__
        return f"[{class_name} ({self.id}) {self.__dict__}]"
