#!/usr/bin/python3
"""Defines Amenity module"""
from models.base_model import BaseModel
import models
import copy


class Amenity(BaseModel):
    """
    inherits from BaseModel and defines Amenity class attributes

    Argument:
            name (str) - empty string
    """

    name = ""

    @staticmethod
    def all():
        """Get all Amenities"""
        obj = models.FileStorage()
        new_obj_dict = copy.deepcopy(obj.all())

        new_obj_dict = {
            k: v for k, v in new_obj_dict.items()
            if k.startswith('Amenity')}

        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        obj_dict = [str(x) for x in new_obj_dict.values()]
        return obj_dict

    @staticmethod
    def count():
        """Count all Amenities"""
        return len(Amenity.all())
