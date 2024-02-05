#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_ref="state")

    @property
    def cities(self):
        return [
            city for city in storage.all("City").values() if city.state_id == self.id
        ]
