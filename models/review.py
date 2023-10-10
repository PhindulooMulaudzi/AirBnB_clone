#!/usr/bin/python3

"""
Review class that inherits BaseModel.

This module defines the Review class,
which represents a review and inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing a review, inheriting from BaseModel.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Review instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
