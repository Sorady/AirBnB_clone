#!/usr/bin/python3
"""Unit tests for state class"""


import unittest
from models.state import State
from models.base_model import BaseModel
import json


class TestState(unittest.TestCase):

    """Test Cases for the State class."""

    def test_instantiation(self):
        """Tests instantiation of State class."""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))


if __name__ == "__main__":
    unittest.main()
