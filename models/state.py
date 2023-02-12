#!/usr/bin/python3
"""Defines State module"""
from models.base_model import BaseModel
from models import helper_functions


class State(BaseModel):
    """
    Inherits from BaseModel and defines state class attributes

    Argument:
        name (str) - empty string
    """

    name = ""

    @staticmethod
    def all():
        """Get all instances"""
        return helper_functions.get_all("State")

    @staticmethod
    def count():
        """Count all class instances"""
        return helper_functions.get_all_count(State)

    @staticmethod
    def show(class_name, instance_id):
        """Show the needed instance"""
        return helper_functions.show_instance(class_name, instance_id)

    @staticmethod
    def destroy(class_name, instance_id):
        """delete specified instance"""
        return helper_functions.delete(class_name, instance_id)
