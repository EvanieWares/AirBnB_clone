#!/usr/bin/python3
"""A Class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances
"""

import json

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
        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, "r") as json_file:
                serialized_objects = json.load(json_file)
            for key, obj_dict in serialized_objects.items():
                class_name, obj_id = key.split(".")
                if class_name == "User":
                    obj = User(**obj_dict)
                else:
                    pass
                self.__object[key] = obj

        except FileNotFoundError:
            pass
