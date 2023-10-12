#!/usr/bin/python3
"""
Review module for the HBNB project.

This module defines the Review class, which represents review information
for places in the HBNB project. It inherits from the BaseModel class and
the Base class for database storage.
"""

import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Review class to store review information.
