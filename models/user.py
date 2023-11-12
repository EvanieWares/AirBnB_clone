#!/usr/bin/python3
"""A class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class for the User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
