from fastapi import APIRouter

from backend.services.analytics_service import (
    get_analytics,
)

router = APIRouter()


@router.get("/analytics")
def analytics():

    return get_analytics()