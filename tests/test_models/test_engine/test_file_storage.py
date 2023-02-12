#!/usr/bin/python3
"""
Defines unittest cases for models.engine.file_storage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class TestFileStorage(unittest.TestCase):
    def test_pri_attr(self):
        b = BaseModel()
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            file_path = fs.__file_path
        with self.assertRaises(AttributeError):
            file_obj = fs.__objects

    def test_all(self):
        """ test for public instance attribute all"""
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_reload(self):
        """test for public instance attribute reload"""
        fs = FileStorage()
        b1 = BaseModel({id: "28ab321"})
        b1.save
        fs.save()
        self.assertEqual(fs.reload(), None)

    def test_new(self):
        """test for public instance attribute new"""
        fs = FileStorage()
        b = BaseModel()
        fs.new(b)
        key = b.__class__.__name__ + "." + b.id
        self.assertEqual(fs.all()[key], b)

    def test_obj_creation(self):
        fs = FileStorage()
        b = BaseModel()
        b.name = "Tessy"
        b.number = 89
        b.save()
        fs.save()
        self.assertEqual(b.name, "Tessy")
        self.assertEqual(b.number, 89)
