#!/usr/bin/python3
"""Unit tests for review class"""


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

    def test_instantiation(self):
        """Tests instantiation of Review class."""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))


if __name__ == "__main__":
    unittest.main()
