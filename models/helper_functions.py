#!/usr/bin/python3
"""Module with share functions"""
import models
import copy


def get_all(class_name_string):
    """Get all from class_name"""
    obj = models.FileStorage()
    new_obj_dict = copy.deepcopy(obj.all())

    new_obj_dict = {
        k: v for k, v in new_obj_dict.items()
        if k.startswith(class_name_string)}

    for value in new_obj_dict.values():
        if '__class__' in value.__dict__.keys():
            del value.__dict__['__class__']
    obj_dict = [str(x) for x in new_obj_dict.values()]

    return obj_dict


def get_all_count(class_name_instance):
    """Count all class_name instances"""
    return len(class_name_instance.all())
