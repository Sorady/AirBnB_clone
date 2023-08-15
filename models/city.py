#!/usr/bin/python3
"""
    This module class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class a city with state_id and name attributes.

    Attributes:
        state_id (str): The ID of the state that the city belongs to.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
