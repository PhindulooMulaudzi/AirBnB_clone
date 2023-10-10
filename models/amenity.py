#!/usr/bin/env python3

"""
Amenity class that inherits BaseModel.

This module defines the Amenity class,
which represents an amenity and inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing an amenity, inheriting from BaseModel.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
