#  Social Media Sentiment Analysis

An end-to-end Machine Learning project that classifies social media posts as **Positive** or **Negative** using Natural Language Processing (NLP). The project is built using the **Sentiment140** dataset and follows a modular pipeline for data preprocessing, feature engineering, model training, evaluation, and prediction.

> **Current Status:** Machine Learning pipeline completed. Backend (FastAPI), MongoDB integration, and frontend are under development.

---

##  Project Overview

Social media platforms generate millions of opinions every day. Analyzing these opinions helps businesses, organizations, and researchers understand public sentiment about products, services, and events.

This project builds a binary sentiment classifier that:

- Cleans and preprocesses raw tweets
- Converts text into numerical features using TF-IDF
- Trains multiple Machine Learning models
- Compares model performance
- Saves the best model for inference
- Predicts sentiment for new user input

---

##  Dataset

**Dataset:** Sentiment140

- **Source:** Kaggle
- **Total Tweets:** 1,600,000
- **Classes:**
  - 0 → Negative
  - 4 → Positive

The dataset contains the following columns:

| Column | Description |
|----------|-------------|
| target | Sentiment label |
| id | Tweet ID |
| date | Tweet timestamp |
| flag | Query flag |
| user | Username |
| text | Tweet content |

---

# 🏗 Project Structure

```text
social-media-sentiment-analysis/
│
├── artifacts/
│
├── backend/
│   ├── database/
│   ├── routes/
│   ├── schemas/
│   └── main.py
│
├── data/
│   └── raw/
│
├── notebooks/
│   └── Social_Media_Sentiment.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- WordCloud
- Joblib

### Machine Learning

- TF-IDF Vectorization
- Logistic Regression
- LinearSVC
- SGDClassifier

### Upcoming

- FastAPI
- MongoDB
- React
- Docker

---

#  Machine Learning Workflow

```text
Raw Tweets
      │
      ▼
Data Loading
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Selection
      │
      ▼
Save Model & Vectorizer
      │
      ▼
Predict New Sentiment
```

---

#  Text Preprocessing

The following preprocessing steps are applied:

- Convert text to lowercase
- Remove URLs
- Remove usernames (@mentions)
- Remove special characters
- Decode HTML entities
- Preserve hashtag words
- Remove extra whitespace
- Convert labels:
  - 0 → Negative
  - 1 → Positive

---

#  Feature Engineering

The cleaned tweets are converted into numerical vectors using **TF-IDF**.

Configuration:

- Maximum Features = 50,000
- N-Grams = (1,2)
- Minimum Document Frequency = 2
- Maximum Document Frequency = 0.95

---

#  Training Data Scaling Experiment

To understand how training size affects model performance, controlled experiments were conducted using a **fixed test set of 50,000 tweets**.

| Training Size | Accuracy | Pipeline Time |
|--------------:|----------:|--------------:|
| 100,000 | 79.72% | 17.61 s |
| 400,000 | 81.07% | 33.17 s |
| 800,000 | **81.52%** | 64.82 s |

**Observation**

Increasing training data improved performance, but gains diminished beyond 400,000 training samples.

---

#  Model Comparison

Three machine learning algorithms were evaluated.

| Model | Accuracy | Macro F1 |
|--------|----------:|----------:|
| Logistic Regression | **81.52%** | **0.8151** |
| LinearSVC | 81.41% | 0.8141 |
| SGDClassifier | 77.55% | 0.7755 |

### Selected Model

 Logistic Regression

Reasons:

- Highest Accuracy
- Highest Macro F1 Score
- Supports probability estimation using `predict_proba()`
- Suitable for deployment

---

#  Model Evaluation

Final Evaluation Results

- Accuracy: **81.52%**
- Macro Precision: **0.8153**
- Macro Recall: **0.8152**
- Macro F1 Score: **0.8151**

---

#  Model Persistence

The trained model and fitted TF-IDF vectorizer are saved using **Joblib**.

Artifacts generated:

```text
artifacts/
│
├── sentiment_model.pkl
└── tfidf_vectorizer.pkl
```

These files are loaded during inference, eliminating the need to retrain the model for every prediction.

---

#  Sample Predictions

| Input | Prediction |
|--------|------------|
| The movie was not good | Negative |
| I thought it would be terrible but I actually loved it | Negative |
| yeah great, exactly what I needed today | Positive |

These examples demonstrate the strengths and limitations of classical TF-IDF based sentiment classifiers, particularly with mixed sentiment and sarcasm.

---

#  Current Progress

- ✅ Data Loading
- ✅ Exploratory Data Analysis
- ✅ Text Preprocessing
- ✅ TF-IDF Feature Engineering
- ✅ Model Training
- ✅ Model Comparison
- ✅ Model Evaluation
- ✅ Model Persistence
- ✅ Prediction Pipeline
- 🔄 FastAPI Backend (In Progress)
- 🔄 MongoDB Integration (Planned)
- 🔄 React Frontend (Planned)
- 🔄 Deployment (Planned)

---

#  How to Run

Clone the repository

```bash
git clone https://github.com/bhumishah28/social-media-sentiment-analysis.git
```

Navigate to the project

```bash
cd social-media-sentiment-analysis
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python src/train.py
```

Run predictions

```bash
python src/predict.py
```

---

#  Future Improvements

- Build REST API using FastAPI
- Integrate MongoDB Atlas
- Develop React frontend
- Add prediction history
- Create analytics dashboard
- Dockerize the application
- Deploy on Render

---

#  Author

**Bhumi Shah**

Computer Science Engineering (Data Science)

DJ Sanghvi College of Engineering

GitHub: https://github.com/bhumishah28