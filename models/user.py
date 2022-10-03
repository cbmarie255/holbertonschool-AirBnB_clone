#!/usr/bin/python3
"""
    User Model, inheriting from BaseModel.
"""
import datetime
import uuid
from models.base_model import BaseModel

class User(BaseModel):
    """user model defined"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """initalizing for future updates"""
        pass
