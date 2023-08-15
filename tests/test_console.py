#!/usr/bin/python3

import unittest
import os
import io
import sys
import json
import models
from console import HBNBCommand
from unittest import mock
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        self.console = None
        try:
            os.remove("file.json")
        except: 
            pass

    def test_create(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create"))
            self.assertTrue(mock_stdout.getvalue() == "** class name missing **\n")
            self.assertFalse(self.console.onecmd("create FakeModel"))
            self.assertTrue(mock_stdout.getvalue() == "** class doesn't exist **\n")
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(len(models.storage.all()) == 2)
            self.assertTrue(self.console.onecmd("create User"))
            self.assertTrue(len(models.storage.all()) == 3)
            self.assertTrue(self.console.onecmd("create State"))
            self.assertTrue(len(models.storage.all()) == 4)
            self.assertTrue(self.console.onecmd("create City"))
            self.assertTrue(len(models.storage.all()) == 5)
            self.assertTrue(self.console.onecmd("create Place"))
            self.assertTrue(len(models.storage.all()) == 6)
            self.assertTrue(self.console.onecmd("create Amenity"))
            self.assertTrue(len(models.storage.all()) == 7)
            self.assertTrue(self.console.onecmd("create Review"))
            self.assertTrue(len(models.storage.all()) == 8)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show(self, mock_stdout):
        self.assertFalse(self.console.onecmd("show"))
        self.assertTrue(mock_stdout.getvalue() == "** class name missing **\n")
        self.assertFalse(self.console.onecmd("show BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "** instance id missing **\n")
        self.assertTrue(self.console.onecmd("show BaseModel " + self.model.id))
        self.assertTrue(mock_stdout.getvalue() == str(self.model) + "\n")
        self.assertFalse(self.console.onecmd("show BaseModel 12345"))
        self.assertTrue(mock_stdout.getvalue() == "** no instance found **\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_all(self, mock_stdout):
        self.assertTrue(self.console.onecmd("all BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "[" + str(self.model) + "]\n")
        self.assertTrue(self.console.onecmd("all"))
        self.assertTrue(mock_stdout.getvalue() == "[" + str(self.model) + "]\n")
        self.assertTrue(self.console.onecmd("all FakeModel"))
        self.assertTrue(mock_stdout.getvalue() == "** class doesn't exist **\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_update(self, mock_stdout):
        self.assertFalse(self.console.onecmd("update"))
        self.assertTrue(mock_stdout.getvalue() == "** class name missing **\n")
        self.assertFalse(self.console.onecmd("update FakeModel"))
        self.assertTrue(mock_stdout.getvalue() == "** class doesn't exist **\n")
        self.assertFalse(self.console.onecmd("update BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "** instance id missing **\n")
        self.assertTrue(self.console.onecmd("update BaseModel " + self.model.id))
        self.assertTrue(mock_stdout.getvalue() == "** attribute name missing **\n")
        self.assertTrue(self.console.onecmd("update BaseModel " + self.model.id + " name"))
        self.assertTrue(mock_stdout.getvalue() == "** value missing **\n")
        self.assertTrue(self.console.onecmd("update BaseModel " + self.model.id + " name \"New Name\""))
        self.assertTrue(self.model.name == "New Name")
        self.assertTrue(mock_stdout.getvalue() == "")


if __name__ == '__main__':
    unittest.main()
