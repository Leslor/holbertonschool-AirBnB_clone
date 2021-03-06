#!/usr/bin/python3
"""
Module that describe the BaseModel class
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        This method return string representation
        """
        cls_n = type(self).__name__
        return (f"[{cls_n}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        This method update attributte with time now
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method return dictionary of all key/value of instance
        """
        dict_new = self.__dict__.copy()
        dict_new["created_at"] = dict_new['created_at'].isoformat()
        dict_new["updated_at"] = dict_new['updated_at'].isoformat()
        dict_new["__class__"] = type(self).__name__
        return (dict_new)
