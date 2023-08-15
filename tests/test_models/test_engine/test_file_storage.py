#!/usr/bin/python3
"""
Test for storage
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    """Test FileStorage Class"""

    def setUp(self):
        """Set up the testing environment"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after testing"""
        try:
            os.remove(FileStorage.__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIs(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        """Test save and reload methods"""
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(obj_key, new_storage._FileStorage__objects)

    def test_reload_nonexistent_file(self):
        """
        Test reload when file does not exist
        """
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)


if __name__ == '__main__':
    unittest.main()
