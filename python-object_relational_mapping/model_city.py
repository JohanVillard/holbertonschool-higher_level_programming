#!/usr/bin/python3
"""This module defines a `City` class."""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Represent a city."""

    __tablename__ = "cities"

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
