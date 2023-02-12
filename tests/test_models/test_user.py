#!/usr/bin/python3
"""
Defines unittest cases for models.user
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def test_attr(self):
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        u.destroy("User", u.id)

    def test_parent(self):
        u = User()
        self.assertTrue(isinstance(u, BaseModel))
        u.destroy("User", u.id)

    def test_count(self):
        """test for count method"""
        u = User()
        count = u.count()
        self.assertIsInstance(count, int)
        u.destroy("User", u.id)

    def test_attr_value(self):
        u = User()
        u.first_name = "Tessy"
        u.last_name = "James"
        u.email = "tessy@gmail.com"
        u.password = "root"
        self.assertEqual(u.first_name, "Tessy")
        self.assertEqual(u.last_name, "James")
        self.assertEqual(u.email, "tessy@gmail.com")
        self.assertEqual(u.password, "root")
        u.destroy("User", u.id)

    def test_show(self):
        """test for show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            u = User()
            u.show("User", u.id)
            self.assertTrue(
                    f"{f.getvalue().strip()}".startswith("[User]"))
            u.destroy("User", u.id)

        with patch("sys.stdout", new=StringIO()) as f:
            u = User()
            ret = u.show("User", "11111")
            self.assertEqual(ret, 0)
            u.destroy("User", u.id)

        with patch("sys.stdout", new=StringIO()) as f:
            u = User()
            ret = u.show("User", u.id)
            self.assertEqual(ret, 1)
            u.destroy("User", u.id)

        with patch("sys.stdout", new=StringIO()) as f:
            u = User()
            u.show("User", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            u.destroy("User", u.id)
