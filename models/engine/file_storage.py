#!/usr/bin/python3
"""
    Serializes & deseralizes instances to a JSON file.
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
            dumpy = json.dumps(my_dict)
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            return f.write(dumpy)

    def reload(self):
        """will reload server data"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                dictionary = json.load(f)
            for key, value in dictionary.items():
                name = value['__class__']
                self.new(eval(name)(**value))
