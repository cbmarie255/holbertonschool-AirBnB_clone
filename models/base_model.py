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
        message = "[{}] ({}) {}".format(self.__class, self.id, self.__dict__)
        return message

    def save(self):
        self.save = save
        save = self.updated_at

    def to_dict(self):
        
        bnb_dict = {
            'id' = self.id,
            'updated_at' = datetime.datetime.strptime(self.updated_at,
                                                      '%Y-%m-%dT%H:%M:%S.%f'),
            'created_at' = datetime.datetime.strptime(self.created_at,
                                                      '%Y-%m-%dT%H:%M:%S.%f'),
            '__class__' = self.__class
            }
        return bnb_dict
