#!/usr/bin/python3
""" The module defines the BaseModel class"""
import copy
from uuid import uuid4
from datetime import datetime
import models
from models import helper_functions


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Arguments:
            id (str) - public instance with  unique value
            created_at - holds current date and time when created
            updated_at - holds current date and time when updated
            *args: unused
            **kwargs - dict representation of key/value pairs
        """
        tf = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None and len(kwargs) != 0:
            if "__class" in kwargs:
                del kwargs["__class__"]
            kwargs['created_at'] = datetime.fromisoformat(
                str(kwargs['created_at']))
            kwargs['updated_at'] = datetime.fromisoformat(
                str(kwargs['updated_at']))
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            date_now = datetime.today()
            self.created_at = date_now
            self.updated_at = date_now
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instances.
        """

        ret_dict = copy.deepcopy(self.__dict__)
        ret_dict["__class__"] = self.__class__.__name__
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        return ret_dict

    def __str__(self):
        """
        prints string representation of instance attributes
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    @staticmethod
    def all():
        """Get all instances"""
        return helper_functions.get_all("BaseModel")

    @staticmethod
    def count():
        """Count all class instances"""
        return helper_functions.get_all_count(BaseModel)

    @staticmethod
    def show(class_name, instance_id):
        """Show the needed instance"""
        return helper_functions.show_instance(class_name, instance_id)

    @staticmethod
    def destroy(class_name, instance_id):
        """delete specified instance"""
        return helper_functions.delete(class_name, instance_id)
