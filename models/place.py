#!/usr/bin/python3
"""
Defines the Place class which inherits
from the BaseModel class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from the BaseModel class
    Represents a Place

    Attributes:
        city_id (str): the City.id
        user_id (str): the User.id
        name (str): the name of the place
        description (str): the description of the place
        number_rooms (int): the number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): the maximum number of guests
        price_by_night (int): the price charged per night
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list: str): a list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
