#!/usr/bin/python3
"""
    This module class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
