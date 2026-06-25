from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import (
    traffic_routes,
    weather_routes,
    target_routes,
    analytics_routes,
    auth_routes
)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include all API routers
app.include_router(traffic_routes.router)
app.include_router(weather_routes.router)
app.include_router(target_routes.router)
app.include_router(analytics_routes.router)
app.include_router(auth_routes.router)


@app.get("/")
def home():
    return {
        "message": "SmartFlow Backend Running"
    }