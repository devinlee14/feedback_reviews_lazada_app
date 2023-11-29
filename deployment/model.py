"""
Graded Challenge 7
Nama: Devin Yaung Lee
Batch: HCK-009
// eda.py //
program ini menjadi base model EDA interface.
"""
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
from keras.models import load_model
import os

# Import the text preprocessing and prediction functions if they are defined elsewhere
from file import text_preprocessing

# Define a function to make predictions
def make_prediction(model, texts, text_preprocessing):
    # Apply custom text preprocessing
    preprocessed_texts = [text_preprocessing(text) for text in texts]

    # Predict using the loaded model
    predictions = model.predict(preprocessed_texts)
    return predictions

def run():
    st.title("Predict the User Sentiment")

    # Check if the model directory exists before loading the model

    model = load_model('model_lstm')

    # User input for review text
    user_input = st.text_area("Enter your review:")

    if st.button('Predict'):
        # Preprocess the user input
        preprocessed_text = text_preprocessing(user_input)

        # Make predictions using the preprocessed data
        predictions = make_prediction(model, [preprocessed_text], text_preprocessing)

        # Convert prediction probabilities to class labels
        predicted_class = np.argmax(predictions, axis=1)[0]

        # Mapping index to class label
        class_labels = {0: 'bad', 1: 'neutral', 2: 'good'}
        predicted_label = class_labels[predicted_class]

        # Display the prediction
        if predicted_label == 'bad':
            st.error("The model predicts the sentiment as bad.")
        elif predicted_label == 'neutral':
            st.warning("The model predicts the sentiment as neutral.")
        else:
            st.success("The model predicts the sentiment as good.")