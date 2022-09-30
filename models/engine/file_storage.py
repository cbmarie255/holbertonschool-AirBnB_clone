#!/usr/bin/python3
"""
    Serializes & deseralizes instances to a JSON file.
"""
import json
from models import BaseModel

class FileStorage:
    """Serializes & deseralizes instances to a JSON file"""
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """Initialization"""
        pass

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
            dump = str({key: value.to_dict})
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            return f.write(dump)

    def reload(self):
        """will reload server data"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_load = json.load(f.read())
        except:
            pass
        for key, value in obj_load.items():
            f.read()
