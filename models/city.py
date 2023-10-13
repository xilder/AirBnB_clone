#!/usr/bin/python3
"""
Defines the City class which inherits
from the BaseModel class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from the BaseModel class
    Represents a City

    Attrributes:
        state_id (str): the State.id
        name (str): the name of the city
    """

    state_id = ""
    name = ""
