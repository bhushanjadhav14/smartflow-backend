from fastapi import APIRouter
from backend.services.weather_service import get_weather

router = APIRouter()


@router.get("/weather-live")
def weather_live():
    return get_weather()