#!/usr/bin/python3
"""
serialises instances in JSON files and deserialises
JSON files into instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    defines the FileStorage for storing and restoring
    instances
    """

    __file_path = "file.json"
    __objects = {}
    model_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State
            }

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
                for k, v in json.load(f).items():
                    if v["__class__"] in self.model_classes:
                        class_name = v["__class__"]
                        self.__objects[k] = self.model_classes[class_name](**v)
        except FileNotFoundError:
            return
