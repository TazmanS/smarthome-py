from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Temperature(Base):
    __tablename__ = 'temperature'

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    ts = Column(DateTime, default=datetime.utcnow)