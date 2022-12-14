#!/usr/bin/python3
""" Base model Module """

import datetime
import uuid
import models
timestamp = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Creates Base Model, define attributes for project """
    def __init__(self, *args, **kwargs):
        """ initializes base instance """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    timestamp)
                elif key == 'updated_at':
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    timestamp)
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ converts to human readable string """
        message = "[{}] ({}) {}".format(self.__class__.__name__, 
                                        self.id, self.__dict__)
        return message

    def save(self):
        """ updates public instance to current date/time """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returing a dictionary containing all keys/values of __dict__ """
        dict_cpy = self.__dict__.copy()
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__
        return dict_cpy
