#!/usr/bin/pythn3
"""Defines City module"""
from models.base_model import BaseModel
import copy
import models


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
        """Get all Cities"""
        obj = models.FileStorage()
        new_obj_dict = copy.deepcopy(obj.all())

        new_obj_dict = {
            k: v for k, v in new_obj_dict.items()
            if k.startswith('City')}

        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        obj_dict = [str(x) for x in new_obj_dict.values()]

        return obj_dict

    @staticmethod
    def count():
        """Count all Cities"""
        return len(City.all())
