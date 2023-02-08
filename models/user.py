#!/usr/bin/python3
""""Defines User module"""
import copy
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    assigns public class attributes that defines users

    Arguments:
                emails (str) - empty string
                password (str) - empty string
                first_name (str) - empty string
                last_name (str) - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @staticmethod
    def all():
        """Get all Users"""
        obj = models.FileStorage()
        new_obj_dict = copy.deepcopy(obj.all())

        new_obj_dict = {
            k: v for k, v in new_obj_dict.items()
            if k.startswith('User')}

        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        obj_dict = [str(x) for x in new_obj_dict.values()]

        return obj_dict

    @staticmethod
    def count():
        """Count all Users"""
        return len(User.all())
