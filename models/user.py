#!/usr/bin/python3
"""Module that describe the User class"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    Class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
