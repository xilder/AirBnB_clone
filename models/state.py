#!/usr/bin/python3
"""
Defines the State class which inherits
from the BaseModel class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from the BaseModel class
    Represents a State

    Attributes:
        name (str): the name of the state
    """

    name = ""
