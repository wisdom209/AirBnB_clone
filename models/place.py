#!/usr/bin/pythn3
"""Defines Place module"""
from models.base_model import BaseModel
import copy
import models


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

    def all():
        """Get all Places"""
        obj = models.FileStorage()
        new_obj_dict = copy.deepcopy(obj.all())

        new_obj_dict = {
            k: v for k, v in new_obj_dict.items()
            if k.startswith('Place')}

        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        obj_dict = [str(x) for x in new_obj_dict.values()]
        print(obj_dict)
