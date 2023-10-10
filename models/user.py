#!/usr/bin/python3

"""
User class that inherits BaseModel.

This module defines the User class,
which represents a user and inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class representing a user, inheriting from BaseModel.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
