#!/usr/bin/python3
""" The module defines the BaseModel class"""
import copy
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Arguments:
                        id (str) - public instance with a unique value
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
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
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
        """Get all from BaseModel"""
        obj = models.FileStorage()
        new_obj_dict = copy.deepcopy(obj.all())

        new_obj_dict = {
            k: v for k, v in new_obj_dict.items()
            if k.startswith('BaseModel')}

        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        obj_dict = [str(x) for x in new_obj_dict.values()]

        return obj_dict

    @staticmethod
    def count():
        """Count all BaseModels"""
        return len(BaseModel.all())
