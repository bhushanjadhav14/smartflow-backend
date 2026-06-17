import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:bhushanjadhav2007@localhost:5432/smart flow db"
)

df = pd.read_csv("data/delhi_traffic_target.csv")

df.columns = [
    "trip_id",
    "travel_time_minutes"
]

df.to_sql(
    "traffic_target",
    engine,
    if_exists="append",
    index=False
)

print("Target data imported successfully!")
print("Rows imported:", len(df))