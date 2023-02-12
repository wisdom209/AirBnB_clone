#!/usr/bin/python3
"""
Defines unittest for models.__init__.py
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage


class TestStorage(unittest.TestCase):
    def test_init_parent(self):
        b = BaseModel()
        s = storage
        self.assertEqual(b.__class__, BaseModel)
        self.assertIsInstance(s, FileStorage)
