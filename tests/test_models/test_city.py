#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from unittest.mock import patch
from io import StringIO


class TestCity(unittest.TestCase):
    def test_attr(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        city.destroy("City", city.id)

    def test_parent(self):
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
        city.destroy("City", city.id)

    def test_all(self):
        """test getting all"""
        b = City()
        all_objects = b.all()
        self.assertIsInstance(all_objects, list)
        b.destroy("City", b.id)

    def test_count(self):
        """testing all count"""
        b = City()
        count = b.count()
        self.assertIsInstance(count, int)
        b.destroy("City", b.id)

    def test_show(self):
        """test the show"""
        with patch('sys.stdout', new=StringIO()) as f:
            b = City()
            b.show("City", b.id)
            self.assertTrue(
                f"{f.getvalue().strip()}".startswith("[City]"))
            b.destroy("City", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = City()
            b.show("City", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            b.destroy("City", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = City()
            ret = b.show("City", "111111")
            self.assertEqual(ret, 0)
            b.destroy("City", b.id)

        with patch('sys.stdout', new=StringIO()) as f:
            b = City()
            ret = b.show("City", b.id)
            self.assertEqual(ret, 1)
            b.destroy("City", b.id)
