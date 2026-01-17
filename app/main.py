from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine
from app.routes.temperature import router as temperature_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("PostgreSQL connected:", result.fetchone())
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(temperature_router)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
