#!/usr/bin/python3
"""
Defines unittest cases fro models.review
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_attr(self):
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")
        r.destroy("Review", r.id)

    def test_parent(self):
        r = Review()
        self.assertTrue(isinstance(r, BaseModel))
        r.destroy("Review", r.id)

    def test_all(self):
        """test for all method"""
        r = Review()
        all_obj = r.all()
        self.assertIsInstance(all_obj, list)
        r.destroy("Review", r.id)

    def test_count(self):
        """test for count method"""
        r = Review()
        count = r.count()
        self.assertIsInstance(count, int)
        r.destroy("Review", r.id)

    def test_show(self):
        """test for show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            r = Review()
            r.show("Review", r.id)
            self.assertTrue(
                    f"{f.getvalue().strip()}".startswith("[Review]"))
            r.destroy("Review", r.id)

        with patch("sys.stdout", new=StringIO()) as f:
            r = Review()
            ret = r.show("Review", "11111")
            self.assertEqual(ret, 0)
            r.destroy("Review", r.id)

        with patch("sys.stdout", new=StringIO()) as f:
            r = Review()
            ret = r.show("Review", r.id)
            self.assertEqual(ret, 1)
            r.destroy("Review", r.id)

        with patch("sys.stdout", new=StringIO()) as f:
            r = Review()
            r.show("Review", "")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            r.destroy("Review", r.id)
