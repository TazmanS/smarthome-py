from fastapi import APIRouter
from app.services.health_service import get_status

router = APIRouter()

@router.get("/")
def root():
    return get_status()