from backend.models.traffic_model import (
    TrafficCount,
    TrafficData,
    AverageSpeed,
    TrafficStats
)







from fastapi import FastAPI
from sqlalchemy import text
from backend.database.db import engine
from backend.services.weather_service import get_weather
from backend.services.traffic_service import (
    get_traffic_count,
    get_traffic_data,
    get_average_speed,
    get_traffic_stats
)
from backend.services.target_service import get_target_count
app = FastAPI()


@app.get("/")
def home():
    return {"message": "SmartFlow Backend Running"}


@app.get("/traffic-count", response_model=TrafficCount)
def traffic_count():
    return get_traffic_count()

from typing import List

@app.get("/dataset-info")
def dataset_info():
    return {
        "features_rows": 4000,
        "target_rows": 4000,
        "target_column": "travel_time_minutes"
    }


@app.get("/weather-live")
def weather_live():
    return get_weather()


@app.get("/target-count")
def target_count():
    return get_target_count()

@app.get("/first-trip")
def first_trip():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT *
                FROM traffic_features
                LIMIT 1
            """)
        )

        row = result.fetchone()

    return {
        "trip_id": row[0],
        "start_area": row[1],
        "end_area": row[2],
        "distance_km": row[3]
    }


@app.get("/total-distance")
def total_distance():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT SUM(distance_km)
                FROM traffic_features
            """)
        )

        total = result.scalar()

    return {
        "total_distance_km": total
    }


@app.get("/area/{area_name}")
def get_area(area_name: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT trip_id, start_area, end_area
                FROM traffic_features
                WHERE start_area = :area
                LIMIT 10
            """),
            {"area": area_name}
        )

        rows = result.fetchall()

    return [dict(row._mapping) for row in rows]


@app.get("/average-speed", response_model=AverageSpeed)
def average_speed():
    return get_average_speed()

@app.get("/traffic-stats", response_model=List[TrafficStats])
def traffic_stats():
    return get_traffic_stats()