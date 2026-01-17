from datetime import datetime

from pydantic import BaseModel


class TemperatureBase(BaseModel):
    value: float

class TemperatureCreate(TemperatureBase):
    pass

class TemperatureRead(TemperatureBase):
    id: int
    ts: datetime

    class Config:
        orm_mode = True
