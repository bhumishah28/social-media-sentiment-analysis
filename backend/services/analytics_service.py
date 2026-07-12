from backend.database.mongodb import predictions_collection


def get_analytics():

    predictions = list(
        predictions_collection.find()
    )

    total_predictions = len(
        predictions
    )

    positive_predictions = sum(
        prediction["sentiment"] == "Positive"
        for prediction in predictions
    )

    negative_predictions = sum(
        prediction["sentiment"] == "Negative"
        for prediction in predictions
    )

    average_confidence = 0

    if total_predictions > 0:

        average_confidence = (
            sum(
                prediction["confidence"]
                for prediction in predictions
            )
            / total_predictions
        )

    positive_percentage = 0

    negative_percentage = 0

    if total_predictions > 0:

        positive_percentage = (
            positive_predictions
            / total_predictions
        ) * 100

        negative_percentage = (
            negative_predictions
            / total_predictions
        ) * 100

    return {

        "total_predictions": total_predictions,

        "positive_predictions": positive_predictions,

        "negative_predictions": negative_predictions,

        "positive_percentage": round(
            positive_percentage,
            2,
        ),

        "negative_percentage": round(
            negative_percentage,
            2,
        ),

        "average_confidence": round(
            average_confidence,
            4,
        ),
    }