from sqlalchemy import text
from backend.database.db import engine


def get_traffic_count():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM traffic_features")
        )

        count = result.scalar()

    return {"total_records": count}

def get_traffic_data():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT trip_id,
                       start_area,
                       end_area,
                       distance_km
                FROM traffic_features
                LIMIT 10
            """)
        )

        rows = result.fetchall()

    data = []

    for row in rows:
        data.append({
            "trip_id": row[0],
            "start_area": row[1],
            "end_area": row[2],
            "distance_km": row[3]
        })

    return data

def get_average_speed():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT AVG(average_speed_kmph)
                FROM traffic_features
            """)
        )

        avg_speed = result.scalar()

    return {
        "average_speed": avg_speed
    }

def get_traffic_stats():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT traffic_density_level,
                       COUNT(*)
                FROM traffic_features
                GROUP BY traffic_density_level
            """)
        )

        rows = result.fetchall()

    return [
        {
            "density": row[0],
            "count": row[1]
        }
        for row in rows
    ]