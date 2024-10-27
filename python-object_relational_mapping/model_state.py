#!/usr/bin/python3
"""This module defines a `State` class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represent a State sql table."""

    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement="auto",
        nullable=False,
        primary_key=True
        )
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")
