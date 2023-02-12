#!/usr/bin/python3
"""
Test suite for amenity class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from io import StringIO
from unittest.mock import patch


class TestAmenity(unittest.TestCase):
    def test_str(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.destroy("Amenity", amenity.id)

    def test_parent(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity))
        amenity.destroy("Amenity", amenity.id)

    def test_all(self):
        """test getting all"""
        b = Amenity()
        all_objects = b.all()
        self.assertIsInstance(all_objects, list)
        b.destroy("Amenity", b.id)

    def test_count(self):
        """testing all count"""
        b = Amenity()
        count = b.count()
        self.assertIsInstance(count, int)
        b.destroy("Amenity", b.id)

    def test_show(self):
        """test the show"""
        with patch('sys.stdout', new=StringIO()) as f:
            b = Amenity()
            b.show("Amenity", b.id)
            self.assertTrue(
                f"{f.getvalue().strip()}".startswith("[Amenity]"))
            b.destroy("Amenity", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = Amenity()
            b.show("Amenity", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            b.destroy("Amenity", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = Amenity()
            ret = b.show("Amenity", "111111")
            self.assertEqual(ret, 0)
            b.destroy("Amenity", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = Amenity()
            ret = b.show("Amenity", b.id)
            self.assertEqual(ret, 1)
            b.destroy("Amenity", b.id)
