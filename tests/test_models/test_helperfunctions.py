#!/usr/bin/python3
"""Helper functions Test module"""
import re
import models
from models import helper_functions
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import copy
import unittest


class TestHelperfunctions(unittest.TestCase):
    """Class tests the helper function module"""

    class_tuple = ("BaseModel", "User", "City", "State",
                   "Amenity", "Place", "Review")

    def test_get_all(self):
        """Test the get all function"""
        result = helper_functions.get_all()
        self.assertIsInstance(result, list)

    def test_get_all_count(self):
        """test get count function"""
        for i in self.class_tuple:
            result = helper_functions.get_all_count(eval(f"{i}"))
            self.assertIsInstance(result, int)

    def test_delete(self):
        """test instance deletion"""
        for i in self.class_tuple:
            result = helper_functions.delete(eval(f"{i}"), 'z')
            self.assertEqual(result, 0)

    def test_show_instance(self):
        """test showing of instance"""
        for i in self.class_tuple:
            result = helper_functions.show_instance(eval(f"{i}"), 'z')
            self.assertEqual(result, 0)

    def test_update_instance(self):
        """testing updating instances"""
        for i in self.class_tuple:
            new_obj = eval(i + '()')
            id = new_obj.id
            helper_functions.update_instance(i, id, "age", 3)
            self.assertEqual(new_obj.age, 3)
            helper_functions.delete(i, id)

    def test_get_do_update_arg_list(self):
        """test get do update arg list"""
        result = helper_functions.get_do_update_arg_list(1, 1, "wisdom")
        self.assertIsInstance(result, list)

    def test_get_needed_params_for_do_update(self):
        """test get neeed params"""
        result = helper_functions.get_needed_params_for_do_update("wis",
                                                                  "name", 1)
        self.assertIsInstance(result, list)
