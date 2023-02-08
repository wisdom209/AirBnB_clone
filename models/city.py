#!/usr/bin/pythn3
"""Defines City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    inherits from BaseModel and defines City class attributes

    Arguments:
        state_id (str) - empty string: it will be the State.id
        name (str) - empty string
    """

    state_id = ""
    name = ""
