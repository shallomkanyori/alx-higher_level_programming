#!/usr/bin/python3
"""This module defines the State class."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represents a state mapped to the states table with a relationship."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", order_by="City.id",
                          cascade="all, delete, delete-orphan")
