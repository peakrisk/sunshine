# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from sunshine.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Station(SurrogatePK, Model):
    """A weather station.

    name: name of the station
    lat:  latitude of the station, float, degrees
    lon:  longitude of the station, float, degrees
    """

    __tablename__ = 'stations'
    name = Column(db.String(80), unique=True, nullable=False)
    lat = Column(db.Float())
    lon = Column(db.Float())
    altitude = Column(db.Float())

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Station({name})>'.format(name=self.name)

class Observation(SurrogatePK, Model):
    """ A weather observation.

    station: id
    time:    date and time of observation
    temperature: temperature in degrees C
    pressure:    pressure reading at location, float, hectopascals or millibars
    humidity:    0.0 - 1.0, with 1.0 meaning 100% humidity, float
    windspeed:   speed of wind in knots
    winddirection: wind direction, 0-360, float, degrees
    """
    

    __tablename__ = 'observations'

    time = Column(db.DateTime(), nullable=False)
    temperature = Column(db.Float(), nullable=True)
    pressure = Column(db.Float(), nullable=True)
    humidity = Column(db.Float(), nullable=True)
    windspeed = Column(db.Float(), nullable=True)
    winddirection = Column(db.Float(), nullable=True)

