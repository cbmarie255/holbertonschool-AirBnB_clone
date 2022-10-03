#!/usr/bin/python3
"""
    User Model, inheriting from BaseModel.
"""
import datetime
import uuid
from models.base_model import BaseModel

class User(BaseModel):
    """user model definded"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initalization of class User to be used in instantiation"""
        super.__init__(*args, **kwargs)
