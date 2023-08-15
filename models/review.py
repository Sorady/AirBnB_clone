#!/usr/bin/python3
"""
    Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that represents a review left by a user for a place.
    Attributes:
        place_id (str): The ID of the place.
        user_id (str): The user_id who left the review.
        text (str): The review content.
    """

    place_id = ""
    user_id = ""
    text = ""
