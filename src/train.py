from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from data_loader import load_data
from preprocessing import preprocess_data


RANDOM_STATE = 42
SAMPLE_SIZE = 100_000
TEST_SIZE = 0.2

MAX_FEATURES = 50_000


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


def train_model():
    """
    Load data, preprocess tweets, create TF-IDF features,
    and train a Logistic Regression sentiment classifier.
    """

    print("Loading dataset...")

    df = load_data(DATA_PATH)

    print("Full dataset shape:", df.shape)


    # Sample data for baseline experimentation
    sample_df = df.sample(
        n=SAMPLE_SIZE,
        random_state=RANDOM_STATE,
    )


    print(
        "Sample dataset shape:",
        sample_df.shape,
    )


    print("Preprocessing tweets...")

    processed_df = preprocess_data(
        sample_df
    )


    X = processed_df["cleaned_text"]
    y = processed_df["target"]


    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=y,
        )
    )


    print(
        "Training samples:",
        len(X_train),
    )

    print(
        "Testing samples:",
        len(X_test),
    )


    print("Creating TF-IDF features...")

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


    print(
        "Training Logistic Regression model..."
    )


    model = LogisticRegression(
        max_iter=1000,
        random_state=RANDOM_STATE,
    )


    model.fit(
        X_train_tfidf,
        y_train,
    )


    print(
        "Training completed successfully."
    )


    return (
        model,
        vectorizer,
        X_test_tfidf,
        y_test,
    )


if __name__ == "__main__":
    train_model()
