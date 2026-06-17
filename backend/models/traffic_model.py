from pydantic import BaseModel


class TrafficCount(BaseModel):
    total_records: int


class TrafficData(BaseModel):
    trip_id: str
    start_area: str
    end_area: str
    distance_km: float


class AverageSpeed(BaseModel):
    average_speed: float


class TrafficStats(BaseModel):
    density: str
    count: int