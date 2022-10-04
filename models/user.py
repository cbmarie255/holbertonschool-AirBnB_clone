#!/usr/bin/python3
"""
    User Model, inheriting from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """user model defined"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
