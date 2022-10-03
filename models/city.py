#!/usr/bin/python3

"""
    City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherited class for the city"""
    state_id = ""
    name = ""
    
    def __init__(self):
        """initalizing for future updates"""
        pass
