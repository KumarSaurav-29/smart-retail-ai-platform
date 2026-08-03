from fastapi import APIRouter, File, UploadFile, Depends

from app.services.image_service import predict_image
from app.security import verify_api_key

router = APIRouter(tags=["🖼️ Image Classification"])


@router.post("/classify-image")
@router.post("/classify-product")
async def classify_image(
    file: UploadFile = File(...),
    api_key: str = Depends(verify_api_key)
):
    return predict_image(file.file)