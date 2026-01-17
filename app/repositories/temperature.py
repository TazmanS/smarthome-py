from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.temperature import Temperature
from app.schemas.temperature import TemperatureCreate


async def get_all_temperatures(db: AsyncSession):
    result = await db.execute(select(Temperature))
    return result.scalars().all()

async def create_temperature(db: AsyncSession, temp: TemperatureCreate):
    db_temp = Temperature(
        value=temp.value,
        created_at = datetime.now(datetime.UTC)
    )
    db.add(db_temp)
    await db.commit()
    await db.refresh(db_temp)
    return db_temp
