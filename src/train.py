import time
from pathlib import Path

import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from src.data_loader import load_data
from src.preprocessing import preprocess_data


# -------------------------
# Configuration
# -------------------------

RANDOM_STATE = 42

TRAIN_SAMPLE_SIZE = 800_000
TEST_SIZE = 50_000

MAX_FEATURES = 50_000


# -------------------------
# Project paths
# -------------------------

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)


DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "social_media_data.csv"
)


ARTIFACTS_DIR = (
    PROJECT_ROOT
    / "artifacts"
)


MODEL_PATH = (
    ARTIFACTS_DIR
    / "sentiment_model.pkl"
)


VECTORIZER_PATH = (
    ARTIFACTS_DIR
    / "tfidf_vectorizer.pkl"
)


# -------------------------
# Data preparation
# -------------------------

def prepare_data(
    train_sample_size=TRAIN_SAMPLE_SIZE,
):

    preparation_start_time = time.time()


    print("\nLoading dataset...")

    df = load_data(DATA_PATH)

    print(
        "Full dataset shape:",
        df.shape,
    )


    print("\nCreating fixed test set...")

    train_pool, test_df = train_test_split(
        df,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["target"],
    )


    print(
        "Training pool shape:",
        train_pool.shape,
    )

    print(
        "Fixed test set shape:",
        test_df.shape,
    )


    print("\nSampling training data...")

    train_df = train_pool.sample(
        n=train_sample_size,
        random_state=RANDOM_STATE,
    )


    print(
        "Training sample shape:",
        train_df.shape,
    )


    print(
        "\nPreprocessing training data..."
    )

    processed_train_df = preprocess_data(
        train_df
    )


    print(
        "Preprocessing test data..."
    )

    processed_test_df = preprocess_data(
        test_df
    )


    X_train = processed_train_df[
        "cleaned_text"
    ]

    y_train = processed_train_df[
        "target"
    ]


    X_test = processed_test_df[
        "cleaned_text"
    ]

    y_test = processed_test_df[
        "target"
    ]


    print("\nCreating TF-IDF features...")

    vectorizer = TfidfVectorizer(
        max_features=MAX_FEATURES,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
        sublinear_tf=True,
    )


    X_train_tfidf = (
        vectorizer.fit_transform(
            X_train
        )
    )


    X_test_tfidf = (
        vectorizer.transform(
            X_test
        )
    )


    print(
        "Training matrix shape:",
        X_train_tfidf.shape,
    )

    print(
        "Testing matrix shape:",
        X_test_tfidf.shape,
    )


    preparation_time = (
        time.time()
        - preparation_start_time
    )


    print(
        f"\nData preparation time: "
        f"{preparation_time:.2f} seconds"
    )


    return (
        X_train_tfidf,
        X_test_tfidf,
        y_train,
        y_test,
        vectorizer,
    )


# -------------------------
# Model training
# -------------------------

def train_model(
    X_train,
    y_train,
):

    print(
        "\nTraining Logistic Regression..."
    )


    training_start_time = time.time()


    model = LogisticRegression(
        max_iter=1000,
        random_state=RANDOM_STATE,
    )


    model.fit(
        X_train,
        y_train,
    )


    training_time = (
        time.time()
        - training_start_time
    )


    print(
        "Training completed successfully."
    )

    print(
        f"Model training time: "
        f"{training_time:.2f} seconds"
    )


    return model


# -------------------------
# Save artifacts
# -------------------------

def save_artifacts(
    model,
    vectorizer,
):

    ARTIFACTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


    joblib.dump(
        model,
        MODEL_PATH,
    )


    joblib.dump(
        vectorizer,
        VECTORIZER_PATH,
    )


    print(
        f"\nModel saved to: "
        f"{MODEL_PATH}"
    )

    print(
        f"Vectorizer saved to: "
        f"{VECTORIZER_PATH}"
    )


# -------------------------
# Main execution
# -------------------------

if __name__ == "__main__":

    (
        X_train_tfidf,
        X_test_tfidf,
        y_train,
        y_test,
        vectorizer,
    ) = prepare_data()


    model = train_model(
        X_train_tfidf,
        y_train,
    )


    save_artifacts(
        model,
        vectorizer,
    )