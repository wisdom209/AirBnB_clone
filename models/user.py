#!/usr/bin/python3
""""Defines User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    assigns public class attributes that defines users

    Arguments:
        emails (str) - empty string
        password (str) - empty string
        first_name (str) - empty string
        last_name (str) - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
