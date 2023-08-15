#!/usr/bin/python3
"""
This module contains the FileStorage class that serializes instances
to a JSON file and deserializes JSON file to instances.
"""

import json


class FileStorage:
    """
    A class that serializes and deserializes instances to a JSON file
    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized instances.
    Methods:
        all(): Returns the dictionary __objects.
        new(obj): Adds a new instance to __objects.
        save(): Serializes __objects to the JSON file.
        reload(): Deserializes the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = class_name.lower()
                    if module_name == "basemodel":
                        module_name = "base_model"
                    module = __import__(
                            "models." + module_name, fromlist=[class_name])
                    obj_class = getattr(module, class_name)
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
