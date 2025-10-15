from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Village(Base):
    __tablename__ = 'villages'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    boundary = Column(Geometry('POLYGON'))  # Village boundary

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    village_id = Column(Integer, ForeignKey('villages.id'))
    timestamp = Column(DateTime)
    value1 = Column(Float)
    value2 = Column(Float)
