# 🛍️ AI-Powered Smart Retail & Customer Intelligence Platform

An end-to-end AI-powered backend platform for modern retail and e-commerce businesses. This project integrates Computer Vision, Natural Language Processing (NLP), Machine Learning, and FastAPI into a single production-style application capable of recognizing returning customers, classifying products, analyzing customer sentiment, and answering customer queries through an intelligent chatbot.

---

# 📌 Project Overview

The primary objective of this project is to develop a unified AI platform that simulates a real-world smart retail solution by combining multiple AI technologies into a single deployable backend.

The platform provides:

- 🖼️ Product Image Classification
- 👤 Customer Face Recognition
- 😊 Customer Sentiment Analysis
- 🤖 AI Customer Support Chatbot
- 📊 Retail Analytics Dashboard
- 🔐 Secure REST APIs using API Key Authentication

---

# 🚀 Features

## 🖼️ Computer Vision

- Product Image Classification using MobileNetV2
- Face Detection and Recognition
- Returning Customer Identification
- Customer Visit Tracking

## 🧠 Natural Language Processing

- Customer Review Sentiment Analysis
- Text Preprocessing using spaCy
- AI Chatbot for Retail FAQs
- Semantic Search using Sentence Transformers

## ⚙️ Backend

- FastAPI REST APIs
- Automatic Swagger Documentation
- Pydantic Request Validation
- Modular Service Architecture
- API Key Authentication

## 📊 Dashboard

- Customer Visit Statistics
- Sentiment Analytics
- Product Prediction Statistics

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

### Backend Framework

- FastAPI

### Machine Learning & Deep Learning

- TensorFlow
- Scikit-learn
- Sentence Transformers

### Computer Vision

- OpenCV
- face_recognition (dlib)

### Natural Language Processing

- spaCy

### Utilities

- NumPy
- Pandas
- Joblib
- Pickle

### Deployment

- Docker
- Uvicorn

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
│
├── logs/
│
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
| POST | `/chatbot` | AI Customer Support Chatbot |
| GET | `/dashboard/stats` | Dashboard Analytics |

---

# 🔐 Authentication

All protected endpoints require an API Key.

Example Request Header:

```http
X-API-Key: your_api_key
```

---

# 📖 API Documentation

Once the FastAPI server is running, interactive API documentation is available at:

```
http://localhost:8000/docs
```

Swagger UI allows users to test every endpoint directly from the browser.

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/KumarSaurav-29/smart-retail-ai-platform.git
```

## Navigate to the Project

```bash
cd smart-retail-ai-platform
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://localhost:8000/docs
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t smart-retail-ai .
```

## Run Docker Container

```bash
docker run -p 8000:8000 smart-retail-ai
```

---

# 📈 Future Scope

- Real-time Video Face Recognition
- Product Recommendation System
- Inventory Prediction using Machine Learning
- Customer Purchase Forecasting
- Cloud Deployment (AWS / GCP / Azure)
- CI/CD Pipeline using GitHub Actions
- Mobile Application Integration
- Advanced Business Analytics Dashboard

---

# 🔒 Ethical Considerations

This project is intended for educational and research purposes.

When deploying AI-based retail systems, the following principles should be followed:

- Obtain customer consent before facial recognition.
- Protect customer privacy and sensitive information.
- Secure biometric data.
- Regularly evaluate fairness and bias in AI models.
- Follow applicable data protection regulations.

---

# 👨‍💻 Author

**Kumar Saurav**

Computer Science Engineering Student

🔗 GitHub: https://github.com/KumarSaurav-29

💼 LinkedIn: https://www.linkedin.com/in/kumar-saurav4953

---

# 🙏 Acknowledgements

This project was developed using the following open-source technologies:

- FastAPI
- TensorFlow
- OpenCV
- face_recognition
- Hugging Face Sentence Transformers
- spaCy
- Scikit-learn
- Docker

---

# 📜 License

This project is developed for educational and academic purposes.
