#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
<<<<<<< HEAD
from mpdels.city import City
=======
>>>>>>> 3bd2172ff55d1511b651817796f96a1c73a024b9
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_STORAGE_TYPE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete,deleteiorphan)

    def __init__(self, *args, **kwargs):
        """Initializes state class"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_STORAGE_TYPE') != "db":
        @property
        def cities(self, value):
            """getter for cities with given state id"""
            city_list = []
            cities = models.storage.all(City)
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
