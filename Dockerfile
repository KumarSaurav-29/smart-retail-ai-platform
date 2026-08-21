# ============================
# Base Image
# ============================
FROM python:3.11.13-bookworm

# Prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# ============================
# Working Directory
# ============================
WORKDIR /app

# ============================
# Install Linux Dependencies
# ============================
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gcc \
    g++ \
    git \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# ============================
# Copy Requirements
# ============================
COPY requirements.txt .

# ============================
# Upgrade pip
# ============================
RUN pip install --upgrade pip

# ============================
# Install Project Dependencies
# ============================
RUN pip install --no-cache-dir -r requirements.txt

# ============================
# Fix setuptools (pkg_resources)
# ============================
RUN pip uninstall -y setuptools
RUN pip install setuptools==80.9.0

# Verify setuptools version
RUN pip show setuptools

# Verify pkg_resources
RUN python -c "import pkg_resources; print('pkg_resources OK')"

# ============================
# Reinstall Face Recognition Packages
# ============================
RUN pip install --force-reinstall --no-cache-dir face-recognition==1.3.0

RUN pip install --force-reinstall --no-cache-dir \
    git+https://github.com/ageitgey/face_recognition_models.git

# Verify face_recognition_models
RUN python -c "import face_recognition_models; print(face_recognition_models.__file__)"

# Verify face_recognition
RUN python -c "import face_recognition; print('face_recognition OK')"

# ============================
# Copy Project Files
# ============================
COPY . .

# ============================
# Expose FastAPI Port
# ============================
EXPOSE 8000

# ============================
# Start FastAPI
# ============================
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]