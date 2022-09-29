#!/usr/bin/python3
""" Base model Module """

import datetime
import uuid


class BaseModel:
    """ Creates Base Model, define attributes for project """
    def __init__(self):
        """ initializes base instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ converts to human readable string """
        message = "[{}] ({}) {}".format(self.__class__, self.id, self.__dict__)
        return message

    def save(self):
        """ updates public instance to current date/time """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returing a dictionary containing all keys/values of __dict__ """
        dict_cpy = self.__dict__.copy()
        dict_cpy['__class__'] = self.__class__.__name__
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        return dict_cpy
