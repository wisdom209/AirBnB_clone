#!/usr/bin/python3
"""Defines review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    inherits from BaseModel and defines the Review class attributes

    Arguments:
        place_id (str) - empty string: it will be the Place.id
        user_id (str) - empty string: it will be the User.id
        text (str) - empty string
    """

    place_id = ""
    user_id = ""
    text = ""