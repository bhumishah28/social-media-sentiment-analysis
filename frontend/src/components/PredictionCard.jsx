function PredictionCard({ result, loading }) {

    if (loading) {

        return (

            <section className="prediction-result">

                <div className="result-card loading-card">

                    <h2>Analyzing...</h2>

                    <p>

                        Our machine learning model is processing your text.

                    </p>

                    <div className="loader"></div>

                </div>

            </section>

        );

    }

    if (!result) return null;

    const confidence = (
        result.confidence * 100
    ).toFixed(2);

    return (

        <section className="prediction-result">

            <div className="result-card">

                <div className="result-header">

                    <div>

                        <p className="label">

                            Prediction

                        </p>

                        <h2>

                            {result.sentiment}

                        </h2>

                    </div>

                    <span

                        className={
                            result.sentiment === "Positive"

                                ? "badge positive"

                                : "badge negative"
                        }

                    >

                        {result.sentiment}

                    </span>

                </div>

                <div className="confidence-section">

                    <div className="confidence-text">

                        <span>

                            Confidence

                        </span>

                        <strong>

                            {confidence}%

                        </strong>

                    </div>

                    <div className="progress">

                        <div

                            className="progress-fill"

                            style={{

                                width: `${confidence}%`,

                            }}

                        ></div>

                    </div>

                </div>

                <div className="text-container">

                    <div className="text-box">

                        <h4>

                            Original Text

                        </h4>

                        <p>

                            {result.text}

                        </p>

                    </div>

                    <div className="text-box">

                        <h4>

                            Cleaned Text

                        </h4>

                        <p>

                            {result.cleaned_text}

                        </p>

                    </div>

                </div>

            </div>

        </section>

    );

}

export default PredictionCard;