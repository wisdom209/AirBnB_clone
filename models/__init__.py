#!/usr/bin/python3
"""initialization to create a unique FileStorage instance for the app"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
