# Sentiment Analysis Projects

This repository contains sentiment analysis projects created using Python, Tkinter, TextBlob, NLTK, and Scikit-learn.

The projects were created to learn:
- Natural Language Processing (NLP)
- Text preprocessing
- Sentiment prediction
- Machine Learning workflows
- GUI development

The repository includes both a simple GUI based sentiment analyzer and an advanced Machine Learning based movie review sentiment analysis project.

## Projects Included


# Simple Sentiment Analysis

This project is a GUI based sentiment analysis application created using Python, Tkinter, and TextBlob.

The user can enter a customer review, and the program predicts whether the sentiment is:
- Positive
- Negative
- Neutral

The project demonstrates basic NLP concepts and sentiment prediction using polarity scores.

### Features

- GUI based application
- Customer review analysis
- Positive, negative, and neutral sentiment prediction
- Real-time sentiment display
- Simple and interactive interface

### Technologies Used

- Python
- Tkinter
- TextBlob

# Movie Review Sentiment Analysis using NLP and Machine Learning

A simple Natural Language Processing (NLP) project that predicts whether a movie review is positive or negative using Python, NLTK, and Machine Learning.

# Features

- Preprocesses movie reviews using NLP
- Removes stopwords and punctuation
- Converts words into their root forms using lemmatization
- Converts text data into numerical vectors using TF-IDF
- Trains a Logistic Regression model
- Predicts sentiment of custom movie reviews
- Saves trained model and vectorizer using Pickle

# Technologies Used

- Python
- NLTK
- Scikit-learn
- Logistic Regression
- TF-IDF Vectorization
- Pickle

# Dataset Used

NLTK Movie Reviews Dataset

Contains:
- Positive movie reviews
- Negative movie reviews

# Project Workflow

1. Load movie review dataset
2. Preprocess the text
3. Tokenize words
4. Remove stopwords and punctuation
5. Lemmatize words
6. Convert text into numerical vectors using TF-IDF
7. Split dataset into training and testing data
8. Train Logistic Regression model
9. Test model accuracy
10. Predict custom reviews
11. Save trained model

# Files

## ML_sentiment_analysis.py
Main Python program containing:
- Data preprocessing
- Model training
- Prediction system

## model.pkl
Saved trained Logistic Regression model.

## vectorizer.pkl
Saved TF-IDF vectorizer used for text conversion.

# Installation

Install required libraries:

pip install nltk
pip install scikit-learn

## How to Run

Run any Python file individually:

python filename.py

Example:

python sentiment_analysis_gui.py

python ML_sentiment_analysis.py

## Accuracy 

The model achieves approximately 80%+ accuracy depending on training split.

## Future Improvements
  Add GUI using Tkinter
  Add Flask web application
  Use Deep Learning models
  Add real-time review analysis
  Improve accuracy using advanced NLP techniques
 
## What I Learned

- Basics of Natural Language Processing
- Text preprocessing techniques
- Sentiment prediction
- Machine Learning workflows
- Tokenization and lemmatization
- Working with NLP datasets
- Model training and testing
- Accuracy evaluation
- GUI development using Tkinter
- Saving trained models using pickle
