#!/usr/bin/python3
"""
Defines unittest cases for models/state.py
"""
import unittest
from io import StringIO
from models.base_model import BaseModel
from models.state import State
from unittest.mock import patch


class TestState(unittest.TestCase):
    def test_attr(self):
        s = State()
        self.assertEqual(s.name, "")

    def test_parent(self):
        s = State()
        self.assertTrue(isinstance(s, BaseModel))
        s.destroy("State", s.id)

    def test_all(self):
        """test for all method"""
        s = State()
        all_obj = s.all()
        self.assertIsInstance(all_obj, list)
        s.destroy("State", s.id)

    def test_count(self):
        """test for count method"""
        s = State()
        count = s.count()
        self.assertIsInstance(count, int)
        s.destroy("State", s.id)

    def test_show(self):
        """test for show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            s = State()
            s.show("State", s.id)
            self.assertTrue(
                    f"{f.getvalue().strip()}".startswith("[State]"))
            s.destroy("State", s.id)

        with patch("sys.stdout", new=StringIO()) as f:
            s = State()
            ret = s.show("State", "11111")
            self.assertEqual(ret, 0)
            s.destroy("State", s.id)

        with patch("sys.stdout", new=StringIO()) as f:
            s = State()
            ret = s.show("State", s.id)
            self.assertEqual(ret, 1)
            s.destroy("State", s.id)

        with patch("sys.stdout", new=StringIO()) as f:
            s = State()
            s.show("State", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            s.destroy("State", s.id)
