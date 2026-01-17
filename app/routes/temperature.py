from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal
from app.schemas.temperature import TemperatureCreate, TemperatureRead
from app.services.temperature_service import add_temperature, list_temperatures

router = APIRouter(
    prefix="/temperatures",
    tags=["temperatures"]
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# --- GET /temperatures ---
@router.get("/", response_model=list[TemperatureRead])
async def get_temperatures(db: AsyncSession = Depends(get_db)):
    return await list_temperatures(db)

# --- POST /temperatures ---
@router.post("/", response_model=TemperatureRead)
async def create_temperature_endpoint(
    temp: TemperatureCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await add_temperature(db, temp)
