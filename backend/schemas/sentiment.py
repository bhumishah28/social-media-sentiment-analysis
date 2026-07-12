from pydantic import BaseModel


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    text: str
    cleaned_text: str
    sentiment: str
    confidence: float