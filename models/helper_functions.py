#!/usr/bin/python3
"""Module with share functions"""
import models
import copy


def get_all(class_name_string=None):
    """Get all from class_name"""
    obj = models.FileStorage()
    new_obj_dict = copy.deepcopy(obj.all())

    if class_name_string:
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


def delete(class_name, instance_id):
    """Delete an instance"""

    obj = models.FileStorage()
    instance_id = instance_id.strip().strip('\"').strip("\'")
    if instance_id == "":
        print("** instance id missing **")
        return 1

    full_key = f"{class_name}.{instance_id}"

    if full_key in obj.all().keys():
        del obj.all()[full_key]
        f = models.FileStorage()
        f.save()
        return 1
    else:
        return 0


def show_instance(class_name, instance_id):
    """show the needed instance"""
    obj = models.FileStorage()
    instance_id = instance_id.strip().strip('\"').strip("\'")
    if instance_id == "":
        print("** instance id missing **")
        return 1

    full_key = f"{class_name}.{instance_id}"
    if full_key in obj.all().keys():
        new_obj_dict = copy.deepcopy(obj.all())
        for value in new_obj_dict.values():
            if '__class__' in value.__dict__.keys():
                del value.__dict__['__class__']
        print(new_obj_dict[full_key])
        return 1
    else:
        return 0


def update_instance(class_name, id, attr_name, attr_value):
    """"Update specified instance"""
    obj = models.FileStorage()
    full_key = f"{class_name}.{id}"

    obj = models.FileStorage()
    obj_to_update = obj.all()[full_key]
    add_val = attr_value
    try:
        add_val = eval(attr_value)
    except Exception:
        pass
    obj_to_update.__dict__[attr_name] = add_val

    obj.save()
