from fastapi import APIRouter, UploadFile, File, Depends

from app.services.face_service import recognize_face
from app.security import verify_api_key

router = APIRouter(tags=["👤 Face Recognition"])


@router.post("/recognize-face")
async def face(
    file: UploadFile = File(...),
    api_key: str = Depends(verify_api_key)
):
    return recognize_face(file.file)