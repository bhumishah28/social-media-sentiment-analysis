import { useEffect, useState } from "react";

import "./index.css";

import Navbar from "./components/Navbar";
import PredictionForm from "./components/PredictionForm";
import PredictionCard from "./components/PredictionCard";
import AnalyticsCard from "./components/AnalyticsCard";
import HistoryTable from "./components/HistoryTable";

import {
  predictSentiment,
  getAnalytics,
  getHistory,
} from "./services/api";

function App() {

  const [result, setResult] = useState(null);

  const [analytics, setAnalytics] = useState(null);

  const [history, setHistory] = useState([]);

  const [loading, setLoading] = useState(false);

  const loadDashboard = async () => {

    try {

      const analyticsData = await getAnalytics();

      const historyData = await getHistory();

      setAnalytics(analyticsData);

      setHistory(historyData);

    }

    catch (error) {

      console.log(error);

    }

  };

  useEffect(() => {

    loadDashboard();

  }, []);

  const handlePrediction = async (text) => {

    try {

      setLoading(true);

      const prediction =
      await predictSentiment(text);

      setResult(prediction);

      await loadDashboard();

    }

    catch (error) {

      console.log(error);

      alert("Prediction Failed");

    }

    finally {

      setLoading(false);

    }

  };

  return (

    <div className="app">

      <div className="background">

        <div className="blob blob1"></div>

        <div className="blob blob2"></div>

        <div className="blob blob3"></div>

      </div>

      <Navbar />

      <section className="hero">

        <span className="tag">

          Machine Learning • FastAPI • MongoDB

        </span>

        <h1>

          Understand
          <br />
          Social Media
          <br />
          Sentiment.

        </h1>

        <p>

          Analyze tweets, reviews and social media
          posts using a machine learning model
          powered by Logistic Regression.

        </p>

      </section>

      <PredictionForm

        onPredict={handlePrediction}

        loading={loading}

      />

      <PredictionCard

        result={result}

        loading={loading}

      />

      <AnalyticsCard

        analytics={analytics}

      />

      <HistoryTable

        history={history}

      />

    </div>

  );

}

export default App;