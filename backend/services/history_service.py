from backend.database.mongodb import predictions_collection


def get_prediction_history():

    predictions = list(
        predictions_collection.find()
    )

    for prediction in predictions:

        prediction["_id"] = str(
            prediction["_id"]
        )

    return predictions