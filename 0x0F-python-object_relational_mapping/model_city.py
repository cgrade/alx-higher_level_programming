#!/usr/bin/python3
"""
A script that contains
City class definiation and
Base Class instantiation
"""

from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    """City Class model, that maps to the `cities` table """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(states.id))
