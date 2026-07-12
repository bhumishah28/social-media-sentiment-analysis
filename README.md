# SentimentScope

A full-stack Machine Learning web application that predicts the sentiment of social media posts using Logistic Regression, FastAPI, MongoDB Atlas, and React.

---

## Features

- Predicts sentiment as **Positive** or **Negative**
- Displays prediction confidence
- Stores every prediction in MongoDB Atlas
- Analytics dashboard with:
  - Total predictions
  - Positive predictions
  - Negative predictions
  - Average confidence
- Recent prediction history
- Modern React frontend
- FastAPI backend
- REST API architecture

---

## Tech Stack

### Machine Learning

- Python
- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer
- NLTK
- Pandas
- NumPy

### Backend

- FastAPI
- Uvicorn
- MongoDB Atlas
- PyMongo

### Frontend

- React
- Vite
- Axios
- CSS3

---

## Project Structure

```text
social-media-sentiment-analysis/

├── artifacts/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── backend/
│   ├── database/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│
├── src/
│   ├── preprocessing.py
│   ├── predict.py
│   ├── train_model.py
│   └── data_loader.py
│
├── data/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/social-media-sentiment-analysis.git

cd social-media-sentiment-analysis
```

---

### Create virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root.

```env
MONGODB_URI=your_connection_string

DATABASE_NAME=SentimentAnalysis

COLLECTION_NAME=predictions
```

---

### Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

Swagger Docs

```
http://localhost:8000/docs
```

---

### Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/predict/` | Predict sentiment |
| GET | `/history` | View recent predictions |
| GET | `/analytics` | View analytics |
| GET | `/health` | Health check |

---

## Screenshots

### Home Page

_Add screenshot here_

### Prediction

_Add screenshot here_

### Analytics Dashboard

_Add screenshot here_

---

## Future Improvements

- User Authentication
- Multi-class Sentiment Analysis
- Deep Learning Models (LSTM/BERT)
- Docker Deployment
- Charts & Visualizations
- Export Prediction History
- Batch Predictions

---

## Author

**Bhumi Shah**

GitHub:
https://github.com/bhumishah28

LinkedIn:
_Add your LinkedIn URL here_

---

## License

This project is licensed under the MIT License.