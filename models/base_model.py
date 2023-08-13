/base_model.py
import uuid
from datetime import datetime

class BaseModel:
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize a new instance of BaseModel"""
        self.id = str(uuid.uuid4()) # assign a unique id as a string
        self.created_at = datetime.now() # assign the current datetime
        self.updated_at = self.created_at # assign the same datetime as created_at

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy() # make a copy of the instance attributes
        result["__class__"] = self.__class__.__name__ # add a key __class__ with the class name
        result["created_at"] = self.created_at.isoformat() # convert created_at to ISO format string
        result["updated_at"] = self.updated_at.isoformat() # convert updated_at to ISO format string
        return result

