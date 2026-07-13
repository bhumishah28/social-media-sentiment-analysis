#  Social Media Sentiment Analysis

A full-stack Machine Learning web application that predicts the sentiment of social media posts in real time using Natural Language Processing (NLP). The application provides instant sentiment prediction, stores prediction history in MongoDB Atlas, and displays real-time analytics through an interactive React dashboard.

---

##  Live Demo

### Frontend
https://social-media-sentiment-analysis-jade.vercel.app/

### Backend API
https://sentimentscope-sbc8.onrender.com

### API Documentation (Swagger)
https://sentimentscope-sbc8.onrender.com/docs

---



##  Features

- Real-time sentiment prediction
- Machine Learning powered NLP model
- TF-IDF Vectorization
- Logistic Regression Classifier
- FastAPI REST API
- React + Vite frontend
- MongoDB Atlas database integration
- Prediction history tracking
- Live analytics dashboard
- Responsive modern UI
- Fully deployed cloud application

---

##  Tech Stack

### Machine Learning

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- NLTK
- NumPy
- Pandas

### Backend

- FastAPI
- Uvicorn
- Pydantic
- MongoDB Atlas
- PyMongo

### Frontend

- React
- Vite
- Axios
- CSS3

### Deployment

- Render (Backend)
- Vercel (Frontend)
- MongoDB Atlas

---

##  Project Structure

```
social-media-sentiment-analysis
│
├── backend
│   ├── database
│   ├── routes
│   ├── schemas
│   ├── services
│   └── main.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── artifacts
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src
│
├── requirements.txt
└── README.md
```

---

##  How It Works

```
User Input
      │
      ▼
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Logistic Regression Model
      │
      ▼
Sentiment Prediction
      │
      ├────────────► MongoDB Atlas
      │                   │
      │                   ▼
      │          Prediction History
      │
      ▼
Frontend Dashboard
```

---

##  API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/predict/` | Predict sentiment |
| GET | `/history` | Prediction history |
| GET | `/analytics` | Analytics summary |

---

##  Machine Learning Pipeline

1. Text Cleaning
2. Tokenization
3. Stopword Removal
4. TF-IDF Feature Extraction
5. Logistic Regression Prediction
6. Confidence Score Generation
7. Store Prediction in MongoDB
8. Display Result on Frontend

---

##  Local Installation

### Clone Repository

```bash
git clone https://github.com/bhumishah28/social-media-sentiment-analysis.git

cd social-media-sentiment-analysis
```

---

### Backend Setup

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn backend.main:app --reload
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

##  Environment Variables

### Backend

Create a `.env` file:

```env
MONGODB_URI=YOUR_MONGODB_URI

DATABASE_NAME=sentiment_db

COLLECTION_NAME=predictions

FRONTEND_ORIGINS=http://localhost:5173
```

---

### Frontend

Create `.env.local`

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Production

```env
VITE_API_BASE_URL=https://sentimentscope-sbc8.onrender.com
```

---


##  Learning Outcomes

This project demonstrates:

- End-to-End Machine Learning Deployment
- NLP Pipeline Development
- FastAPI REST API Development
- React Frontend Development
- MongoDB Atlas Integration
- Cloud Deployment
- REST API Integration
- Production-ready Project Structure

---

##  Author

**Bhumi Shah**

GitHub

https://github.com/bhumishah28
