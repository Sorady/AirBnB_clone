#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

"""Developer: Sorady & Beshoy"""

"""A module that defines a base class for all other classes"""


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    for other classes

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The timestamp indicating when
        the instance was created.
        updated_at (datetime): The timestamp indicating when
        the instance was last updated.

    Methods:
        __init__(): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the instance.
        save(): Updates the updated_at attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
