#!/usr/bin/python3

"""Unit tests for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
import json
import os


FileStorage = file_storage.FileStorage
classes = {"BaseModel": BaseModel, }

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage Class"""
    def test_all_function(self):
        """Tests for the all fuction that it returns the dictionary
        """
        storage = file_storage.FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)


    def test_save_function(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
