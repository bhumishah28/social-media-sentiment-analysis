import { useState } from "react";

function PredictionForm({ onPredict, loading }) {

    const [text, setText] = useState("");

    const handleSubmit = () => {

        if (!text.trim()) {

            alert("Please enter some text.");

            return;

        }

        onPredict(text);

        setText("");

    };

    return (

        <section className="prediction-section">

            <div className="prediction-box">

                <h2>

                    Analyze Sentiment

                </h2>

                <p>

                    Paste any tweet, review or social media post and let the model predict its sentiment.

                </p>

                <textarea

                    value={text}

                    onChange={(e) =>
                        setText(e.target.value)
                    }

                    placeholder="Example: I absolutely loved the cinematography but the ending felt rushed..."

                />

                <div className="prediction-footer">

                    <span>

                        {text.length} Characters

                    </span>

                    <button

                        onClick={handleSubmit}

                        disabled={loading}

                    >

                        {

                            loading

                            ?

                            "Analyzing..."

                            :

                            "Analyze Sentiment"

                        }

                    </button>

                </div>

            </div>

        </section>

    );

}

export default PredictionForm;