from pathlib import Path

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Models directory
MODELS_DIR = BASE_DIR / "models"

# Image Classification
IMAGE_MODEL = MODELS_DIR / "best_image_classifier.keras"
CLASS_NAMES = MODELS_DIR / "class_names.json"

# Sentiment Analysis
SENTIMENT_MODEL = MODELS_DIR / "sentiment_model.pkl"
TFIDF_VECTORIZER = MODELS_DIR / "tfidf_vectorizer.pkl"

# Chatbot
CHATBOT_EMBEDDINGS = MODELS_DIR / "chatbot_embeddings.pkl"
CHATBOT_KNOWLEDGE = MODELS_DIR / "chatbot_knowledge.pkl"

# Face Recognition
FACE_ENCODINGS = MODELS_DIR / "face_encodings.pkl"
KNOWN_NAMES = MODELS_DIR / "known_names.pkl"