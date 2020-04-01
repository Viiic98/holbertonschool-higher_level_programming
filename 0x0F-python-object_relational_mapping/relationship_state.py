#!/usr/bin/python3
""" State Model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Table states """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    # Build a relationship between the table that is in the class City
    # Using backref don't need to create the relationship inside the other
    # class, but using back_populates we need to create it
    cities = relationship("City", backref="state", cascade="all, delete")
