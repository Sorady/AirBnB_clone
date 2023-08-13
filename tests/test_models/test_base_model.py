#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        self.base_model = BaseModel()

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_instance_methods(self):
        """Test instance methods"""
        self.assertTrue(hasattr(self.base_model, '__str__'))
        self.assertTrue(hasattr(self.base_model, 'save'))
        self.assertTrue(hasattr(self.base_model, 'to_dict'))

    def test_str_method(self):
        """Test __str__ method"""
        string_representation = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(string_representation, str(self.base_model))

    def test_save_method(self):
        """Test save method"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        to_dict_result = self.base_model.to_dict()
        self.assertEqual(type(to_dict_result), dict)
        self.assertIn('__class__', to_dict_result)
        self.assertIn('created_at', to_dict_result)
        self.assertIn('updated_at', to_dict_result)
        self.assertIn('id', to_dict_result)

    def test_to_dict_updated_at(self):
        """Test if updated_at is ISO formatted"""
        to_dict_result = self.base_model.to_dict()
        updated_at = self.base_model.updated_at.isoformat()
        self.assertEqual(to_dict_result['updated_at'], updated_at)

    def test_to_dict_created_at(self):
        """Test if created_at is ISO formatted"""
        to_dict_result = self.base_model.to_dict()
        created_at = self.base_model.created_at.isoformat()
        self.assertEqual(to_dict_result['created_at'], created_at)


if __name__ == '__main__':
    unittest.main()
