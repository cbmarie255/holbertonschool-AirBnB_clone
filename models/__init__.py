#!/usr/bin/python3
"""
    __init__ file
"""


from models.engine.file_storage import storage
storage = FileStorage()
storage.reload()
