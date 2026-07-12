function HistoryTable({ history }) {

    if (!history || history.length === 0) {

        return (

            <section
                className="history-section"
                id="history"
            >

                <div className="section-heading">

                    <h2>

                        Recent Predictions

                    </h2>

                    <p>

                        No predictions available yet.

                    </p>

                </div>

            </section>

        );

    }

    return (

        <section
            className="history-section"
            id="history"
        >

            <div className="section-heading">

                <h2>

                    Recent Predictions

                </h2>

                <p>

                    Latest sentiment predictions stored in MongoDB.

                </p>

            </div>

            <div className="history-list">

                {

                    history.map((item) => (

                        <div
                            className="history-card"
                            key={item._id}
                        >

                            <div className="history-top">

                                <span
                                    className={
                                        item.sentiment === "Positive"
                                            ? "badge positive"
                                            : "badge negative"
                                    }
                                >

                                    {item.sentiment}

                                </span>

                                <span className="confidence">

                                    {(item.confidence * 100).toFixed(2)}%

                                </span>

                            </div>

                            <p className="history-text">

                                {item.text}

                            </p>

                            <small>

                                {new Date(
                                    item.timestamp
                                ).toLocaleString()}

                            </small>

                        </div>

                    ))

                }

            </div>

        </section>

    );

}

export default HistoryTable;