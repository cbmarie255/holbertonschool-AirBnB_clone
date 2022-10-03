#!/usr/bin/python3
"""
    Serializes & deseralizes instances to a JSON file.
"""
import json
import os


class FileStorage:
    """Serializes & deseralizes instances to a JSON file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """set in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """will serialize objects to the obj with a key"""
        for key, value in self.__objects.items():
            dumpy = str({key: value.to_dict()})
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            f.write(dumpy)

    def reload(self):
        """will reload server data"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                loady = json.load(f.read())
            objs = eval(loady)
            for key, value in objs.items():
                objs[key] = eval(key.split('.')[0] + '(**value)')
            self.__objects = objs
        except:
            pass
