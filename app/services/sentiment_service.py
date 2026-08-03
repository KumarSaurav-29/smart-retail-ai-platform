import app.startup as startup


def analyze_sentiment(text: str):
    """
    Predict sentiment using the trained Logistic Regression model.
    """

    # Convert text into TF-IDF features
    text_vector = startup.tfidf_vectorizer.transform([text])

    # Predict class
    prediction = startup.sentiment_model.predict(text_vector)[0]

    # Predict probabilities
    probabilities = startup.sentiment_model.predict_proba(text_vector)[0]

    confidence = max(probabilities)

    sentiment = "Positive" if prediction == 1 else "Negative"

    return {
        "sentiment": sentiment,
        "confidence": round(float(confidence) * 100, 2)
    }