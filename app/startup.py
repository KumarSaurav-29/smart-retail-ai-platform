from sentence_transformers import SentenceTransformer
import json
import joblib
import pickle
import tensorflow as tf

from app.config import (
    IMAGE_MODEL,
    CLASS_NAMES,
    SENTIMENT_MODEL,
    TFIDF_VECTORIZER,
    CHATBOT_EMBEDDINGS,
    CHATBOT_KNOWLEDGE,
    FACE_ENCODINGS,
    KNOWN_NAMES,
)

# =========================
# Global Variables
# =========================

image_model = None
class_names = None

sentiment_model = None
tfidf_vectorizer = None

chatbot_embeddings = None
chatbot_knowledge = None
embedding_model = None

face_encodings = None
known_names = None


# =========================
# Load All AI Models
# =========================

def load_models():
    global image_model
    global class_names

    global sentiment_model
    global tfidf_vectorizer

    global chatbot_embeddings
    global chatbot_knowledge
    global embedding_model

    global face_encodings
    global known_names

    # -------------------------
    # Image Classification
    # -------------------------
    print("Loading Image Classification Model...")

    image_model = tf.keras.models.load_model(IMAGE_MODEL)

    with open(CLASS_NAMES, "r") as f:
        class_names = json.load(f)

    print("Image Classification Model Loaded.")

    # -------------------------
    # Sentiment Analysis
    # -------------------------
    print("Loading Sentiment Analysis Model...")

    sentiment_model = joblib.load(SENTIMENT_MODEL)
    tfidf_vectorizer = joblib.load(TFIDF_VECTORIZER)

    print("Sentiment Model Loaded.")

    # -------------------------
    # Chatbot
    # -------------------------
    print("Loading Chatbot Knowledge Base...")

    with open(CHATBOT_EMBEDDINGS, "rb") as f:
        chatbot_embeddings = pickle.load(f)

    with open(CHATBOT_KNOWLEDGE, "rb") as f:
        chatbot_knowledge = pickle.load(f)

    print("Loading Sentence Transformer...")

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Chatbot Loaded.")

    # -------------------------
    # Face Recognition
    # -------------------------
    print("Loading Face Recognition Data...")

    with open(FACE_ENCODINGS, "rb") as f:
        face_encodings = pickle.load(f)

    with open(KNOWN_NAMES, "rb") as f:
        known_names = pickle.load(f)

    print("Face Recognition Loaded.")

    # -------------------------
    # Done
    # -------------------------
    print("\n✅ All AI Models Loaded Successfully!")