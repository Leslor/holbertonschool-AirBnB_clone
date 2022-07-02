#!/usr/bin/python3
"""Module that describe the Review class"""

from models.base_model import BaseModel
import models


class Review(BaseModel):
    """
    Class Review that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
