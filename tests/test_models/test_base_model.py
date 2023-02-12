#!/usr/bin/python3
"""
Test suite for base_model
"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the base_model
    """

    def test_all(self):
        """test getting all"""
        b = BaseModel()
        all_objects = b.all()
        self.assertIsInstance(all_objects, list)
        b.destroy("BaseModel", b.id)

    def test_count(self):
        """testing all count"""
        b = BaseModel()
        count = b.count()
        self.assertIsInstance(count, int)
        b.destroy("BaseModel", b.id)

    def test_show(self):
        """test the show"""
        with patch('sys.stdout', new=StringIO()) as f:
            b = BaseModel()
            b.show("BaseModel", b.id)
            self.assertTrue(
                f"{f.getvalue().strip()}".startswith("[BaseModel]"))
            b.destroy("BaseModel", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = BaseModel()
            b.show("BaseModel", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            b.destroy("BaseModel", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = BaseModel()
            ret = b.show("BaseModel", "111111")
            self.assertEqual(ret, 0)
            b.destroy("BaseModel", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = BaseModel()
            ret = b.show("BaseModel", b.id)
            self.assertEqual(ret, 1)
            b.destroy("BaseModel", b.id)

    def test_class_init(self):
        """tests initialization"""
        b = BaseModel()
        b.name = "me"
        b.number = 98
        self.assertEqual(b.name, "me")
        self.assertEqual(b.number, 98)
        b.destroy("BaseModel", b.id)

    def test_str(self):
        """
        checks the string output of an instance
        """
        base = BaseModel()
        self.assertEqual(
            base.__str__(),
            f"[{type(base).__name__}] ({base.id}) {base.__dict__}")
        base.destroy("BaseModel", base.id)

    def test_to_dict(self):
        """
        checks the to_dict() function of an instance
        """
        base = BaseModel()
        prev_time = base.updated_at
        self.assertDictEqual(base.to_dict(),
                             {'__class__': type(base).__name__,
                              'updated_at': base.updated_at.isoformat(),
                              'id': base.id,
                              'created_at': base.created_at.isoformat()})
        base.save()
        self.assertNotEqual(prev_time, base.updated_at)
        base.destroy("BaseModel", base.id)

    def test_attr_classes(self):
        """
        checks if the right classes were use to generate attributes
        """
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)
        base.destroy("BaseModel", base.id)
        base2.destroy("BaseModel", base2.id)

    def test_save(self):
        """
        tests the save method
        """
        base = BaseModel()
        prevtime = base.updated_at
        base.save()
        newtime = base.updated_at
        self.assertNotEqual(prevtime, newtime)
        base.destroy("BaseModel", base.id)
