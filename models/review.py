#!/usr/bin/python3

"""
    Review module
"""
import models.base_model import BaseModel


class Review(BaseModel):
    """inherited class for the state"""
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self):
        """initalizing for future updates"""
        pass
