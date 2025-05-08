import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load the dataset
def load_data():
    # Your CSV file with intents
    data = pd.read_csv("intent_datasetp.csv")
    return data

# Train the model to classify the intent
def train_intent_classifier():
    data = load_data()
    X = data['text']  # Text column
    y = data['intent']  # Intent column

    # Create a machine learning pipeline with CountVectorizer and Naive Bayes
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X, y)  # Train the model on the dataset
    return model

# Function to process user input and predict the intent
def process_input(user_input):
    model = train_intent_classifier()  # Train the model (or load a pre-trained model)
    predicted_intent = model.predict([user_input])[0]  # Predict the intent of the user input
    return predicted_intent