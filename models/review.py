#!/usr/bin/python3
"""Defines review module"""
from models.base_model import BaseModel
from models import helper_functions


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
        """Get all class instances"""
        return helper_functions.get_all("Review")

    @staticmethod
    def count():
        """Count all class instances"""
        return helper_functions.get_all_count(Review)

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
