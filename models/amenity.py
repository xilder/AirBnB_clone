#!/usr/bin/python3
"""
Defines the Amenity class which inherits
from the BaseModel class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from the BaseModel class
    Represents an Amenity

    Attributes:
        name (str): the name of the amenity
    """

    name = ""
