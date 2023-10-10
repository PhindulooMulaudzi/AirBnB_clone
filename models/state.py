#!/usr/bin/python3

"""
State class that inherits BaseModel.

This module defines the State class,
which represents a state and inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representing a state, inheriting from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
