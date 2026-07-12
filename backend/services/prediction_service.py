from datetime import datetime

from backend.database.mongodb import predictions_collection
from src.predict import predict_sentiment


def predict_and_save(text: str):

    # Predict sentiment
    result = predict_sentiment(text)

    # Add timestamp
    result["timestamp"] = datetime.utcnow()

    # Save to MongoDB
    predictions_collection.insert_one(result)

    return result