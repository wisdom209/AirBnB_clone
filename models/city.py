#!/usr/bin/pythn3
"""Defines City module"""
from models.base_model import BaseModel
from models import helper_functions


class City(BaseModel):
    """
    inherits from BaseModel and defines City class attributes

    Arguments:
                    state_id (str) - empty string: it will be the State.id
                    name (str) - empty string
    """

    state_id = ""
    name = ""

    @staticmethod
    def all():
        """Get all class instances"""
        return helper_functions.get_all("City")

    @staticmethod
    def count():
        """Count all class instances"""
        return helper_functions.get_all_count(City)
