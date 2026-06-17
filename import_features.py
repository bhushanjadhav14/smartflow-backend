import pandas as pd
from sqlalchemy import create_engine

# Replace YOUR_PASSWORD with your PostgreSQL password
engine = create_engine(
    "postgresql://postgres:bhushanjadhav2007@localhost:5432/smart flow db"
)

df = pd.read_csv("data/delhi_traffic_features.csv")

# Column names in CSV -> column names in PostgreSQL
df.columns = [
    "trip_id",
    "start_area",
    "end_area",
    "distance_km",
    "time_of_day",
    "day_of_week",
    "weather_condition",
    "traffic_density_level",
    "road_type",
    "average_speed_kmph"
]

df.to_sql(
    "traffic_features",
    engine,
    if_exists="append",
    index=False
)

print("Data imported successfully!")
print("Rows imported:", len(df))
