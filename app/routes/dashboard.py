from collections import Counter
import csv
import os

from fastapi import APIRouter, Depends

from app.security import verify_api_key

router = APIRouter(tags=["📊 Dashboard Analytics"])

LOG_FILE = "logs/visits.csv"


@router.get("/dashboard/stats")
def dashboard_stats(
    api_key: str = Depends(verify_api_key)
):

    if not os.path.exists(LOG_FILE):

        return {
            "total_visits": 0,
            "unique_customers": 0,
            "most_frequent_customer": None,
            "average_confidence": 0
        }

    names = []
    confidences = []

    with open(LOG_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            names.append(row["Name"])
            confidences.append(float(row["Confidence"]))

    total_visits = len(names)

    unique_customers = len(set(names))

    most_frequent = Counter(names).most_common(1)

    if most_frequent:
        most_frequent_customer = most_frequent[0][0]
    else:
        most_frequent_customer = None

    average_confidence = (
        round(sum(confidences) / len(confidences), 2)
        if confidences else 0
    )

    return {
        "total_visits": total_visits,
        "unique_customers": unique_customers,
        "most_frequent_customer": most_frequent_customer,
        "average_confidence": average_confidence
    }