import csv
import os
from datetime import datetime

import numpy as np
import face_recognition

import app.startup as startup


LOG_FILE = "logs/visits.csv"


def log_visit(name, confidence):
    """
    Log every recognized customer visit.
    """

    os.makedirs("logs", exist_ok=True)

    # Create CSV with header if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Name",
                "Date",
                "Time",
                "Confidence"
            ])

    now = datetime.now()

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            round(float(confidence), 2)
        ])


def recognize_face(file):
    """
    Recognize a customer's face from an uploaded image.
    """

    image = face_recognition.load_image_file(file)

    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 0:
        return {
            "recognized": False,
            "message": "No face detected."
        }

    face_encodings = face_recognition.face_encodings(
        image,
        face_locations
    )

    encoding = face_encodings[0]

    matches = face_recognition.compare_faces(
        startup.face_encodings,
        encoding,
        tolerance=0.5
    )

    face_distances = face_recognition.face_distance(
        startup.face_encodings,
        encoding
    )

    best_match_index = np.argmin(face_distances)

    if matches[best_match_index]:

        confidence = (1 - face_distances[best_match_index]) * 100
        confidence = round(float(confidence), 2)

        person = startup.known_names[best_match_index]

        # Log recognized visit
        log_visit(person, confidence)

        return {
            "recognized": True,
            "person": person,
            "confidence": confidence
        }

    return {
        "recognized": False,
        "message": "Unknown Person"
    }