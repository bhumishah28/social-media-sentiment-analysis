from fastapi import APIRouter

from backend.services.history_service import (
    get_prediction_history,
)

router = APIRouter()


@router.get("/history")
def get_history():

    return get_prediction_history()