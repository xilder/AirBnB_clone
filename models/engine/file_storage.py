#!/usr/bin/python3
"""
serialises instances in JSON files and deserialises
JSON files into instances
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    defines the FileStorage for storing and restoring
    instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary self.__objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets a new object in self._objects using the
        obj.id as the key
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        saves self.__objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[k] = v.to_dict()
            json.dump(json_dict, f)

    def reload(self):
        """
        loads JSON file to self.__objects
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
