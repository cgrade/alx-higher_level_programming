#!/usr/bin/python3
"""
A script that contains
state class definiation and
Base Class instantiation
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class model, that maps to the `state` table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
