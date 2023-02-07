#!/usr/bin/python3
"""Defines the FileStorage class"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    serializes instances to a json file and deserializes json file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        oclasname = obj.__class__.__name__
        BaseModel.__objects["{}.{}".format(oclasname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        ocdict = FileStorage.__objects
        objdict = {obj: ocdict[obj].to_dict() for obj in ocdict.keys()}
        with open(FileStorage.__file_path, "w+") as fp:
            json.dump(objdict, fp)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(FileStorage.__file_path, "r") as fp:
                objdict = json.loads(fp.read())
        except FileNotFoundError:
            pass
