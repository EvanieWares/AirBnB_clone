#!/usr/bin/python3
"""A Class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """A class that serializes instances to JSON"""
    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Returns dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as jf:
            json.dump(serialized_objects, jf)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as jf:
                serialized_objects = json.load(jf)
            for key, obj_dict in serialized_objects.items():
                self.new(eval(key.split(".")[0])(**obj_dict))
        except FileNotFoundError:
            pass
