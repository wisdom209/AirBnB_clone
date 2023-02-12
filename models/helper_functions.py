#!/usr/bin/python3
"""Module with share functions"""
import re
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
    if instance_id == "" or not instance_id:
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


def get_do_update_arg_list(do_update, isDotUpdate, line):
    """get a list for performing do_update action"""
    args = None
    to_update = do_update
    quoted_attr_value = None
    if isDotUpdate:
        args = line.split(", ")
    else:
        new_line = line + " "
        # match: <classname> <id> <attr_name> "<attr_value>"
        str_regex = re.compile(
            r"^\w+\s+[\w\-]+\s+\w+\s+([\"\'][\w\s]+[\"\']\s)")
        str_match = str_regex.match(new_line)
        if (str_match):
            quoted_attr_value = str_match.group(1)
        if (not quoted_attr_value and "'" in line) or \
                (not quoted_attr_value and '"' in line):
            to_update = 0
        args = line.split()
    return [args, to_update, quoted_attr_value]


def get_needed_params_for_do_update(args, quoted_attr_value, do_update):
    """Get parameters needed to update an object"""
    class_name = None
    id = None
    attr_name = None
    attr_value = None
    tot_args = len(args)
    for i in range(tot_args):
        if i == 0:
            class_name = args[0].strip().strip('\"').strip("\'")
        if i == 1:
            id = args[1].strip().strip('\"').strip("\'")
        if i == 2:
            attr_name = args[2].strip().strip('\"').strip("\'")
        if i == 3:
            if quoted_attr_value:
                attr_value = quoted_attr_value.strip()
            else:
                attr_value = args[3].strip()
                # check if value contains only digits
                check_quote_reg = re.compile(r"(^\'.*\'$)|(^\".*\"$)")
                check_quote_match = check_quote_reg.match(attr_value)
                if not check_quote_match:
                    for x in attr_value:
                        if not x.isdigit():
                            do_update = 0
                    if do_update:
                        attr_value = int(attr_value)
    retList = [class_name, id, attr_name, attr_value, do_update]
    return retList
