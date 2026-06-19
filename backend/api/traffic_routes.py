from fastapi import APIRouter
from typing import List

from backend.services.traffic_service import (
    get_traffic_count,
    get_traffic_data,
    get_average_speed,
    get_traffic_stats
)

from backend.models.traffic_model import (
    TrafficCount,
    TrafficData,
    AverageSpeed,
    TrafficStats
)

router = APIRouter()


@router.get("/traffic-count", response_model=TrafficCount)
def traffic_count():
    return get_traffic_count()


@router.get("/traffic-data", response_model=List[TrafficData])
def traffic_data():
    return get_traffic_data()


@router.get("/average-speed", response_model=AverageSpeed)
def average_speed():
    return get_average_speed()


@router.get("/traffic-stats", response_model=List[TrafficStats])
def traffic_stats():
    return get_traffic_stats()