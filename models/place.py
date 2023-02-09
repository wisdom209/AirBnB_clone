#!/usr/bin/pythn3
"""Defines Place module"""
from models.base_model import BaseModel
from models import helper_functions


class Place(BaseModel):
    """
    inherits from BaseModel and defines the Place class attributes

    Arguments:
    city_id (str) - empty string: it will be the City.id
    user_id (str) - empty string: it will be the User.id
    name (str) - empty string
    description (str) - empty string
    number_rooms (int) - 0
    number_bathrooms (int) - 0
    max_guest (int) - 0
    price_by_night (int) - 0
    latitude (float) - 0.0
    longitude (float) - 0.0
    amenity_ids: list of string(empty): it will be the list of Amenity.id
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

    @staticmethod
    def all():
        """Get all class instances"""
        return helper_functions.get_all("Place")

    @staticmethod
    def count():
        """Count all class instances"""
        return helper_functions.get_all_count(Place)

    @staticmethod
    def show(class_name, instance_id):
        """Show the needed instance"""
        return helper_functions.show_instance(class_name, instance_id)
