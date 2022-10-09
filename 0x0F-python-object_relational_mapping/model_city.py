#!/usr/bin/python3
"""
Create a City class and maps it to the states table
"""


from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
