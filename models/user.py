#!/usr/bin/python3
"""
The User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents a user in the system.
    Attributes:
        email (str): User Email.
        password (str): User Password.
        first_name (str): User F name.
        last_name (str): User L name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
