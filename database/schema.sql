-- SmartFlow Database Schema

-- Table: traffic_features

CREATE TABLE traffic_features (
    trip_id VARCHAR(50),
    start_area VARCHAR(100),
    end_area VARCHAR(100),
    distance_km FLOAT,
    average_speed_kmph FLOAT,
    traffic_density_level VARCHAR(50)
);


-- Table: traffic_target

CREATE TABLE traffic_target (
    travel_time_minutes FLOAT
);