#!/usr/bin/python3

"""Class User that inherits from BaseModel."""


from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a user and inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialise the Base Class with the recieved arguments."""
        # Call the superclass's __init__ method to inherit attributes
        super().__init__(*args, **kwargs)
