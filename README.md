# Social Media Sentiment Analysis  
### An End-to-End Data Analytics & Machine Learning Project

---

## Project Overview

This project analyzes social media text data to understand sentiment patterns and builds machine learning models to predict sentiment from tweet text.  
It combines **exploratory data analysis (EDA)**, **natural language processing (NLP)**, and **machine learning**, while addressing real-world challenges such as **class imbalance**.

---

## Problem Statement

Social media platforms generate large volumes of user-generated text that reflect public opinion.  
The goal of this project is to analyze sentiment patterns in social media posts and evaluate whether textual features can be effectively used to predict sentiment.

---

## Objectives

- Analyze sentiment distribution in social media text data  
- Explore linguistic differences between positive and negative sentiment  
- Perform exploratory data analysis using visualizations  
- Build and evaluate machine learning models for sentiment classification  
- Handle class imbalance and analyze precision–recall trade-offs  

---

## Dataset

- **Source:** Twitter Sentiment Dataset  
- **Columns:**
  - `id` – Unique identifier for each tweet  
  - `tweet` – Text content of the tweet  
  - `label` – Sentiment label  
    - `0` → Negative  
    - `1` → Positive  

The dataset is **highly imbalanced**, with negative tweets forming the majority class.

---

## Tools & Technologies Used

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- NLTK (text preprocessing)  
- Scikit-learn  
- TF-IDF Vectorization  
- Logistic Regression  
- Naive Bayes  

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

- Sentiment distribution visualization  
- Text cleaning (lowercasing, punctuation removal, stopword removal)  
- Word frequency analysis for positive and negative sentiment  
- Tweet length comparison by sentiment  
- Word clouds for visualizing common terms  

### Key EDA Insights

- Positive tweets tend to be slightly longer and more expressive.  
- Negative sentiment is often driven by politically or socially charged language.  
- Positive sentiment is associated with emotions, gratitude, and everyday life experiences.  

---

## Machine Learning Models

### Models Implemented

1. Logistic Regression (Baseline)  
2. Logistic Regression with Class Weighting  
3. Logistic Regression with Threshold Tuning  
4. Naive Bayes Classifier  

---

## Handling Class Imbalance

Because the dataset is highly imbalanced, accuracy alone was not a reliable evaluation metric.  
To address this:

- **Class-weighted Logistic Regression** was used to penalize mistakes on the minority class.  
- **Threshold tuning** was tested to study precision–recall trade-offs.  

---

## Model Evaluation Summary

| Model | Precision (Positive) | Recall (Positive) | Accuracy |
|-----|---------------------|------------------|----------|
| Baseline Logistic Regression | High | Low | High |
| **Class-Weighted Logistic Regression** | Moderate | **High** | Good |
| Threshold Tuned Model | Low | Very High | Moderate |
| Naive Bayes | High | Low | High |

### Final Model Selection

**Class-weighted Logistic Regression** was selected as the final model because it provides the best balance between recall and precision, making it more suitable for real-world imbalanced sentiment classification.

---

## Conclusion

This project demonstrates a complete sentiment analysis pipeline—from data cleaning and exploratory analysis to machine learning modeling and evaluation.  
It highlights the importance of:
- Understanding data imbalance  
- Evaluating models beyond accuracy  
- Making informed, justified model selection decisions  

---

## Future Improvements

- Use domain-specific or brand-specific sentiment datasets  
- Apply advanced NLP models such as Word2Vec or BERT  
- Deploy the model using Streamlit or FastAPI  

---

## How to Run the Project

1. Clone the repository  
2. Open the notebook in Google Colab or Jupyter Notebook  
3. Install required libraries  
4. Run the notebook cells sequentially  

---

## Author

Built as a learning-focused data science project to strengthen understanding of NLP, EDA, and machine learning fundamentals.
