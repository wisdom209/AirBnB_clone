#!/usr/bin/python3
"""
Defines unittest cases for place.py
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    def test_attr(self):
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

    def test_parent(self):
        p = Place()
        self.assertTrue(isinstance(p, BaseModel))
        p.destroy("Place", p.id)

    def test_all(self):
        """test for all method"""
        p = Place()
        all_obj = p.all()
        self.assertIsInstance(all_obj, list)
        p.destroy("Place", p.id)

    def test_count(self):
        """test for count method"""
        p = Place()
        count = p.count()
        self.assertIsInstance(count, int)
        p.destroy("Place", p.id)

    def test_show(self):
        """test for show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            p = Place()
            p.show("Place", p.id)
            self.assertTrue(
                    f"{f.getvalue().strip()}".startswith("[Place]"))
            p.destroy("Place", p.id)

        with patch("sys.stdout", new=StringIO()) as f:
            p = Place()
            ret = p.show("Place", "11111")
            self.assertEqual(ret, 0)
            p.destroy("Place", p.id)

        with patch("sys.stdout", new=StringIO()) as f:
            p = Place()
            ret = p.show("Place", p.id)
            self.assertEqual(ret, 1)
            p.destroy("Place", p.id)

        with patch("sys.stdout", new=StringIO()) as f:
            p = Place()
            p.show("Place", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            p.destroy("Place", p.id)
