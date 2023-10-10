#!/usr/bin/env python3

"""
City class that inherits BaseModel.

This module defines the City class,
which represents a city and inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city, inheriting from BaseModel.

    Attributes:
        state_id (str): The state ID associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
