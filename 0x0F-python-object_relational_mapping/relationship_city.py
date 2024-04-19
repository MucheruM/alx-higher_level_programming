#!/usr/bin/python3

"""A module that defines the City Object class"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Defines the City object."""

    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
        )

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeingKey("states.id"), nullable=False)