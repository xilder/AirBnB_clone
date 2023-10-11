#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

"""
Defines the BaseModel cladd
"""


class BaseModel:
    """
    The BaseModel class of the AirBnB project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises an instance of the class
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """
        a string representation of an instance
        of the class
        """
        cls_name = self.__class__.__name__

        return f"[{cls_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        saves the changes made to an instances with the
        time updated
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary representation of the class
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict
