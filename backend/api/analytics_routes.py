from fastapi import APIRouter
from sqlalchemy import text

from backend.database.db import engine


router = APIRouter()


@router.get("/dataset-info")
def dataset_info():
    return {
        "features_rows": 4000,
        "target_rows": 4000,
        "target_column": "travel_time_minutes"
    }


@router.get("/first-trip")
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


@router.get("/total-distance")
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


@router.get("/area/{area_name}")
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

    return [
        dict(row._mapping)
        for row in rows
    ]