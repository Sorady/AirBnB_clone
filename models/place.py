#!/usr/bin/python3
"""
    This module contains Place class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that represents a place with various attributes.

    Attributes:
        city_id (str): The city
        user_id (str): the user_id who owns the place.
        name (str): Place Name.
        description (str): Place Description.
        number_rooms (int): How many Room on the place.
        number_bathrooms (int): How many Bathrooms in place .
        max_guest (int): Maximum number of guests.
        price_by_night (int): night Price.
        latitude (float): Location Latitude.
        longitude (float): Location Longitude.
        amenity_ids (list): the amenities_ids available in the place.
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
