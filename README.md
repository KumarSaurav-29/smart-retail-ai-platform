# 🛍️ AI-Powered Smart Retail & Customer Intelligence Platform

An AI-powered backend platform that combines Computer Vision, Natural Language Processing (NLP), Machine Learning, and FastAPI to simulate a modern smart retail ecosystem. The platform recognizes returning customers, classifies retail products, analyzes customer sentiment, provides intelligent chatbot assistance, and exposes all functionalities through secure REST APIs.

---

# 📌 Project Overview

The objective of this project is to build a unified AI-driven platform capable of solving multiple real-world retail challenges using Artificial Intelligence.

The platform integrates multiple AI domains into a single backend application, including image classification, face recognition, customer sentiment analysis, conversational AI, and retail analytics.

---

# 🎥 Project Demonstration

A short demonstration video showcasing the working application is included in this repository.

📁 **Location:** `demo/demo.mp4`

The demonstration highlights:

- Product Image Classification
- Face Recognition
- Sentiment Analysis
- AI Chatbot
- FastAPI Backend

---

# 🚀 Key Features

## 🖼️ Computer Vision

- Product Image Classification using MobileNetV2
- Face Detection and Face Recognition
- Returning Customer Identification
- Customer Visit Tracking

## 🧠 Natural Language Processing

- Customer Review Sentiment Analysis
- Text Preprocessing using spaCy
- AI-powered Customer Support Chatbot
- Semantic Search using Sentence Transformers

## ⚙️ Backend Services

- FastAPI REST APIs
- Modular Service Architecture
- Pydantic Request Validation
- API Key Authentication
- Automatic Swagger Documentation

## 📊 Analytics Dashboard

- Customer Visit Statistics
- Product Classification Statistics
- Sentiment Analytics

---

# 🧠 AI Models Used

| Module | Model |
|---------|------|
| Product Classification | MobileNetV2 (TensorFlow/Keras) |
| Face Recognition | face_recognition (dlib) |
| Sentiment Analysis | TF-IDF + Logistic Regression |
| Chatbot | Sentence Transformers |
| NLP | spaCy |

---

# 🛠️ Technology Stack

### Programming Language

- Python

### Backend

- FastAPI
- Uvicorn

### Computer Vision

- OpenCV
- face_recognition (dlib)

### Machine Learning & Deep Learning

- TensorFlow
- Scikit-learn
- Sentence Transformers

### Natural Language Processing

- spaCy

### Utilities

- NumPy
- Pandas
- Joblib
- Pickle

### Containerization

- Docker

---

# 📂 Project Structure

```text
smart-retail-ai-platform/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── utils/
│   ├── models/
│   ├── config.py
│   ├── startup.py
│   ├── pipeline.py
│   ├── security.py
│   └── main.py
│
├── models/
├── logs/
├── Dockerfile
├── requirements.txt
├── README.md
├── .dockerignore
└── .gitignore
```

---

# 🔗 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/classify-product` | Product Image Classification |
| POST | `/recognize-face` | Customer Face Recognition |
| POST | `/analyze-sentiment` | Customer Sentiment Analysis |
| POST | `/chatbot` | AI Customer Support |
| GET | `/dashboard/stats` | Dashboard Analytics |

---

# 🔐 Security

The backend uses **API Key Authentication** to secure protected REST endpoints and simulate production-style API access.

---

# 📖 API Documentation

Interactive API documentation is automatically generated using **Swagger UI**.

```
http://localhost:8000/docs
```

Swagger provides an interface to explore and test all available API endpoints.

---

# 🐳 Docker Support

The backend is containerized using Docker for consistent deployment across environments.

Project includes:

- Dockerfile
- requirements.txt
- Docker-based application configuration

---

# 📈 Future Scope

- Real-time Video Face Recognition
- Product Recommendation System
- Inventory Prediction
- Customer Purchase Forecasting
- Cloud Deployment (AWS / GCP / Azure)
- CI/CD Integration
- Mobile Application Support
- Advanced Retail Analytics Dashboard

---

# 🔒 Ethical Considerations

This project is developed for educational and research purposes.

When deploying AI systems in real-world retail environments, organizations should:

- Obtain customer consent before using facial recognition.
- Protect customer privacy and sensitive information.
- Secure biometric and customer data.
- Evaluate AI models for fairness and bias.
- Follow applicable data protection regulations.

---

# 🌟 Project Highlights

- AI-powered Smart Retail Platform
- Modular FastAPI Architecture
- Computer Vision using OpenCV & MobileNetV2
- Face Recognition using dlib
- NLP using spaCy & Sentence Transformers
- Sentiment Analysis using Machine Learning
- Secure REST APIs with API Key Authentication
- Interactive Swagger Documentation
- Docker-ready Backend

---

# 👨‍💻 Author

**Kumar Saurav**

Computer Science Engineering Student

🔗 GitHub: https://github.com/KumarSaurav-29

💼 LinkedIn: https://www.linkedin.com/in/kumar-saurav4953

---

# 📜 License

This project is developed for educational and academic purposes.