from fastapi import FastAPI
from app.api.routes import router
from app.core.config import APP_NAME

app = FastAPI(
    title=APP_NAME,
    version="0.1.0"
)

app.include_router(router)