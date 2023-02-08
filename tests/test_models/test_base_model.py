#!/usr/bin/python3
'''Test BaseModel module'''
from models.base_model import BaseModel
import unittest

class Test_BaseModel(unittest.TestCase):
    '''Test BaseModel class'''
    def test_class_init(self):
        b = BaseModel()
        b.name = "me"
        b.number= 98
        self.assertEqual(b.name, "me")
        self.assertEqual(b.number, 98)
