from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from backend.routes.prediction import (
    router as prediction_router,
)

from backend.routes.history import (
    router as history_router,
)

from backend.routes.analytics import (
    router as analytics_router,
)

app = FastAPI(
    title="Social Media Sentiment Analysis API",
    description="API for predicting sentiment from social media text.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------
# Root Endpoint
# ---------------------------------

@app.get("/")
def root():

    return {
        "message": "Welcome to the Social Media Sentiment Analysis API!"
    }


# ---------------------------------
# Health Check Endpoint
# ---------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# ---------------------------------
# Register Routers
# ---------------------------------

app.include_router(
    prediction_router,
    prefix="/predict",
    tags=["Prediction"],
)

app.include_router(
    history_router,
    tags=["History"],
)

app.include_router(
    analytics_router,
    tags=["Analytics"],
)