from sqlalchemy import text
from backend.database.db import engine


def get_target_count():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM traffic_target")
        )

        count = result.scalar()

    return {
        "total_target_records": count
    }