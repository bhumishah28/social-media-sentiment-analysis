import os

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

allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_origin_regex=r"https://.*\.vercel\.app",
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
# Register appRouters
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