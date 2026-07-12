from fastapi import APIRouter

from backend.schemas.sentiment import (
    SentimentRequest,
    SentimentResponse,
)

from backend.services.prediction_service import predict_and_save


router = APIRouter()


@router.post(
    "/",
    response_model=SentimentResponse,
)
def predict(request: SentimentRequest):

    result = predict_and_save(
        request.text
    )

    return result