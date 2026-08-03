from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.pipeline import pipeline

# Import Routers
from app.routes.image import router as image_router
from app.routes.sentiment import router as sentiment_router
from app.routes.chatbot import router as chatbot_router
from app.routes.face import router as face_router
from app.routes.dashboard import router as dashboard_router


# Load all AI models when the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    pipeline.initialize()
    yield


# Create FastAPI App
app = FastAPI(
    title="🛍️ AI-Powered Smart Retail & Customer Intelligence Platform",
    description="""
An AI-powered backend for modern retail stores that integrates multiple Artificial Intelligence modules into a single FastAPI application.

## Features

- 🖼️ Product Image Classification
- 👤 Face Recognition
- 😊 Customer Sentiment Analysis
- 🤖 AI Customer Support Chatbot
- 📊 Dashboard Analytics
- 🔐 API Key Authentication

## Technologies

- FastAPI
- TensorFlow
- OpenCV
- Scikit-learn
- Sentence Transformers
- Face Recognition (dlib)

## Authentication

All protected endpoints require the following header:

**X-API-Key: smart-retail-2026**
""",
    version="1.0.0",
    lifespan=lifespan,
)


# Register API Routes
app.include_router(image_router)
app.include_router(sentiment_router)
app.include_router(chatbot_router)
app.include_router(face_router)
app.include_router(dashboard_router)


# Home Endpoint
@app.get("/", tags=["🏠 Home"])
def home():
    return {
        "project": "AI-Powered Smart Retail & Customer Intelligence Platform",
        "version": "1.0.0",
        "status": "Running",
        "documentation": "/docs",
        "authentication": "Use header: X-API-Key = smart-retail-2026",
        "modules": [
            "Image Classification",
            "Face Recognition",
            "Sentiment Analysis",
            "AI Chatbot",
            "Dashboard Analytics"
        ]
    }


# Health Check Endpoint
@app.get("/health", tags=["🏠 Home"])
def health():
    return {
        "status": "healthy",
        "message": "All AI services are running successfully."
    }