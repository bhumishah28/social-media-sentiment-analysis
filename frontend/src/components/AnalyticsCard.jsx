function AnalyticsCard({ analytics }) {

    if (!analytics) return null;

    return (

        <section
            className="analytics-section"
            id="analytics"
        >

            <div className="section-heading">

                <h2>

                    Analytics Dashboard

                </h2>

                <p>

                    Real-time insights generated from all stored predictions.

                </p>

            </div>

            <div className="analytics-grid">

                <div className="analytics-item">

                    <span>

                        Total Predictions

                    </span>

                    <h2>

                        {analytics.total_predictions}

                    </h2>

                </div>

                <div className="analytics-item">

                    <span>

                        Positive

                    </span>

                    <h2>

                        {analytics.positive_predictions}

                    </h2>

                </div>

                <div className="analytics-item">

                    <span>

                        Negative

                    </span>

                    <h2>

                        {analytics.negative_predictions}

                    </h2>

                </div>

                <div className="analytics-item">

                    <span>

                        Avg. Confidence

                    </span>

                    <h2>

                        {(analytics.average_confidence * 100).toFixed(2)}%

                    </h2>

                </div>

            </div>

        </section>

    );

}

export default AnalyticsCard;