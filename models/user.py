#!/usr/bin/python3

"""Class User that inherits from BaseModel."""


from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a user and inherits from BaseModel."""

    def __init__(self):
        """Initialize a new User instance with empty values for attributes."""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
