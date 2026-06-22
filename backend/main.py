from fastapi import FastAPI

from backend.api import (
    traffic_routes,
    weather_routes,
    target_routes,
    analytics_routes
)


app = FastAPI()


# Include all API routers
app.include_router(traffic_routes.router)
app.include_router(weather_routes.router)
app.include_router(target_routes.router)
app.include_router(analytics_routes.router)


@app.get("/")
def home():
    return {
        "message": "SmartFlow Backend Running"
    }