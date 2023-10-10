#!/usr/bin/python3

"""
Initialize a unique storage instance for the application.

This module creates a unique storage instance using FileStorage
from the models.engine module, and reloads data if available.
"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Reload data if available
storage.reload()
