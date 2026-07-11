from pathlib import Path

import joblib

from preprocessing import clean_text


# -------------------------
# Paths
# -------------------------

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)


MODEL_PATH = (
    PROJECT_ROOT
    / "artifacts"
    / "sentiment_model.pkl"
)


VECTORIZER_PATH = (
    PROJECT_ROOT
    / "artifacts"
    / "tfidf_vectorizer.pkl"
)


# -------------------------
# Load artifacts
# -------------------------

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(
    VECTORIZER_PATH
)


# -------------------------
# Prediction function
# -------------------------

def predict_sentiment(text):

    cleaned_text = clean_text(text)

    text_tfidf = vectorizer.transform(
        [cleaned_text]
    )

    prediction = model.predict(
        text_tfidf
    )[0]

    probabilities = model.predict_proba(
        text_tfidf
    )[0]

    confidence = probabilities.max()


    if prediction == 1:
        sentiment = "Positive"

    else:
        sentiment = "Negative"


    return {
        "text": text,
        "cleaned_text": cleaned_text,
        "sentiment": sentiment,
        "confidence": round(
            float(confidence),
            4,
        ),
    }


# -------------------------
# Temporary local testing
# -------------------------

if __name__ == "__main__":

    test_text = input(
        "Enter a sentence: "
    )

    result = predict_sentiment(
        test_text
    )

    print("\nPrediction Result")

    print(
        "Original text:",
        result["text"],
    )

    print(
        "Cleaned text:",
        result["cleaned_text"],
    )

    print(
        "Sentiment:",
        result["sentiment"],
    )

    print(
        "Confidence:",
        result["confidence"],
    )