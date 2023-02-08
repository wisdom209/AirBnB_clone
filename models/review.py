#!/usr/bin/python3
"""Defines review module"""
from models.base_model import BaseModel
import copy
import models


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

    @staticmethod
    def all():
        """Get all Reviews"""
        obj = models.FileStorage()
        new_obj_dict = copy.deepcopy(obj.all())

        new_obj_dict = {
            k: v for k, v in new_obj_dict.items()
            if k.startswith('Review')}

        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        obj_dict = [str(x) for x in new_obj_dict.values()]
        return obj_dict

    @staticmethod
    def count():
        """Count all Reviews"""
        return len(Review.all())
