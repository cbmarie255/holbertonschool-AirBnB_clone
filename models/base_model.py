#!/usr/bin/python3
""" Base model Module """

import datetime
import uuid


class BaseModel:
    """ Creates Base Model, define attributes for project """
    ident = str(uuid.uuid4(id))

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = BaseModel.ident

    def __init__(self, created_at=None):
        self.created_at = created_at
        if created_at is None:
            self.created_at = datetime.now()

    def __init__(self, updated_at=None):
        self.updated_at = updated_at
        if updated_at is None:
            self.updated_at = datetime.now()

    def __str__(self):
        message = "[{}] ({}) {}".format(self__class, self.id, self__dict__)
        return message
