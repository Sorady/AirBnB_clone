#!/usr/bin/python3
""""
The module is responsible for creating an instance of the FileStorage class that can be used to store files in the application.
""""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
