#!/usr/bin/python3
"""Unit tests for place class"""


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

    def test_instantiation(self):
        """Tests instantiation of Place class."""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))


if __name__ == "__main__":
    unittest.main()
