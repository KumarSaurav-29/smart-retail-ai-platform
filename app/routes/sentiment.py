from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.sentiment_service import analyze_sentiment
from app.security import verify_api_key

router = APIRouter(tags=["😊 Sentiment Analysis"])


class SentimentRequest(BaseModel):
    text: str


@router.post("/analyze-sentiment")
async def sentiment(
    request: SentimentRequest,
    api_key: str = Depends(verify_api_key)
):
    return analyze_sentiment(request.text)