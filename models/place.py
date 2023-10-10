#!/usr/bin/python3

"""
Place class that inherits BaseModel.

This module defines the Place class,
which represents a place and inherits from BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class representing a place, inheriting from BaseModel.

    Attributes:
        city_id (str): The city ID associated with the place.
        user_id (str): The user ID associated with the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests for the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of amenity IDs associated with the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Place instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
