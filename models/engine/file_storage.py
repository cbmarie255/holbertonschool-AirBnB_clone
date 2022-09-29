#!/usr/bin/python3
"""
    Serializes & deseralizes instances to a JSON file.
"""
import json


class FileStorage:
    """Serializes & deseralizes instances to a JSON file"""
    def __init__(self):
        self.__file_path = file_path
        self.__objects = objects
        self.obj = obj
        self.__class__.__name__ = class_name
        self.id = id

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """set in __objects the obj with key <obj class name>.id"""
        for element on obj:


