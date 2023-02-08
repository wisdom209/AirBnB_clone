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
        FileStorage.__objects["{}.{}".format(oclasname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        """Save/serialize obj dictionaries to json file"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:

            with open(FileStorage.__file_path, "r", encoding='UTF-8') as fp:
                objdict = json.loads(fp.read())

            for key, value in objdict.items():
                obj = BaseModel(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
