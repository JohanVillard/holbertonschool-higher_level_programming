#!/usr/bin/python3
"""This module defines a `State` class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represent a State sql table."""

    __tablename__ = "states"
    __table_args__ = { "mysql_charset": "latin1"}

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True
        )
    name = Column(String(128), nullable=False)

    # Define the relationship to City
    cities = relationship("City", back_populates="state")
