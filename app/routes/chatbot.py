from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.chatbot_service import chatbot_response
from app.security import verify_api_key

router = APIRouter(tags=["🤖 AI Chatbot"])


class ChatbotRequest(BaseModel):
    question: str


@router.post("/chatbot")
async def chatbot(
    request: ChatbotRequest,
    api_key: str = Depends(verify_api_key)
):
    return chatbot_response(request.question)