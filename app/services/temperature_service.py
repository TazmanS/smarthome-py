from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.temperature import create_temperature, get_all_temperatures
from app.schemas.temperature import TemperatureCreate


async def list_temperatures(db: AsyncSession):
    temps = await get_all_temperatures(db)
    return temps

async def add_temperature(db: AsyncSession, temp_create: TemperatureCreate):
    if not (-50 <= temp_create.value <= 100):
        raise ValueError("Temperature out of realistic range!")
    new_temp = await create_temperature(db, temp_create)
    return new_temp
