#!/usr/bin/python3
"""Defines Amenity module"""
from models.base_model import BaseModel
from models import helper_functions


class Amenity(BaseModel):
    """
    inherits from BaseModel and defines Amenity class attributes

    Argument:
                                    name (str) - empty string
    """

    name = ""

    @staticmethod
    def all():
        """Get all instances"""
        return helper_functions.get_all("Amenity")

    @staticmethod
    def count():
        """Count all class instances"""
        return helper_functions.get_all_count(Amenity)

    @staticmethod
    def show(class_name, instance_id):
        """Show the needed instance"""
        return helper_functions.show_instance(class_name, instance_id)

    @staticmethod
    def destroy(class_name, instance_id):
        """delete specified instance"""
        return helper_functions.delete(class_name, instance_id)

    @staticmethod
    def update(class_name, instance_id, attr_name, attr_value):
        """update specified instance"""
        return helper_functions.delete(class_name, instance_id,
                                       attr_name, attr_value)
