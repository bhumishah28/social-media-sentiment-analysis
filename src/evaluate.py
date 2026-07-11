import time

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
)

from train import (
    prepare_data,
    train_models,
)


def evaluate_model(
    model,
    X_test,
    y_test,
):
    """
    Evaluate one trained model.
    """

    evaluation_start_time = time.time()


    predictions = model.predict(
        X_test
    )


    accuracy = accuracy_score(
        y_test,
        predictions,
    )


    precision, recall, f1, _ = (
        precision_recall_fscore_support(
            y_test,
            predictions,
            average="macro",
        )
    )


    report = classification_report(
        y_test,
        predictions,
        target_names=[
            "Negative",
            "Positive",
        ],
    )


    matrix = confusion_matrix(
        y_test,
        predictions,
    )


    evaluation_time = (
        time.time()
        - evaluation_start_time
    )


    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "report": report,
        "confusion_matrix": matrix,
        "evaluation_time": evaluation_time,
    }


if __name__ == "__main__":

    # Prepare data only once
    (
        X_train_tfidf,
        X_test_tfidf,
        y_train,
        y_test,
        vectorizer,
        preparation_time,
    ) = prepare_data()


    # Train all models
    (
        trained_models,
        training_times,
    ) = train_models(
        X_train_tfidf,
        y_train,
    )


    results = {}


    # Evaluate all models
    for model_name, model in (
        trained_models.items()
    ):

        print(
            "\n"
            + "=" * 60
        )

        print(
            f"Evaluating: {model_name}"
        )

        print(
            "=" * 60
        )


        result = evaluate_model(
            model,
            X_test_tfidf,
            y_test,
        )


        results[
            model_name
        ] = result


        print(
            f"\nAccuracy: "
            f"{result['accuracy']:.4f}"
        )

        print(
            f"Macro Precision: "
            f"{result['precision']:.4f}"
        )

        print(
            f"Macro Recall: "
            f"{result['recall']:.4f}"
        )

        print(
            f"Macro F1: "
            f"{result['f1_score']:.4f}"
        )


        print(
            "\nClassification Report:"
        )

        print(
            result["report"]
        )


        print(
            "Confusion Matrix:"
        )

        print(
            result["confusion_matrix"]
        )


        print(
            f"\nModel training time: "
            f"{training_times[model_name]:.2f} seconds"
        )

        print(
            f"Evaluation time: "
            f"{result['evaluation_time']:.2f} seconds"
        )


    # Final comparison
    print(
        "\n\n"
        + "=" * 70
    )

    print(
        "FINAL MODEL COMPARISON"
    )

    print(
        "=" * 70
    )


    print(
        f"\n{'Model':<25}"
        f"{'Accuracy':<12}"
        f"{'F1':<12}"
        f"{'Train Time':<15}"
    )


    print(
        "-" * 64
    )


    for model_name, result in (
        results.items()
    ):

        print(
            f"{model_name:<25}"
            f"{result['accuracy']:<12.4f}"
            f"{result['f1_score']:<12.4f}"
            f"{training_times[model_name]:<15.2f}"
        )


    print(
        f"\nShared data preparation time: "
        f"{preparation_time:.2f} seconds"
    )