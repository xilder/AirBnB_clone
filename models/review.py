#!/usr/bin/python3
"""
Defines the Review class which inherits
from the BaseModel class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from the BaseModel class
    Represents a Review

    Attributes:
        place_id (str): the Place.id
        user_id (str): the User.id
        text (str): the review text
    """

    place_id = ""
    user_id = ""
    text = ""
