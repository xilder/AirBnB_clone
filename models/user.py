#!/usr/bin/python3
"""
Defines the User class which inherits
from the BaseModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class
    Represents a User

    Attributes:
        email (str): the user's email
        password (str): the user's password
        first_name (str): the user's first name
        last_name (str): the user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
