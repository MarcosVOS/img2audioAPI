from fastapi import APIRouter, Depends, UploadFile, HTTPException
from app.application.services.image_to_text_service import ImageToTextService
from app.dependencies.image_to_text_provider import get_image_to_text_service
from app.domain.models.image import Image
from typing import Annotated

router = APIRouter()

@router.post("/img2text")
async def img2text(
    file: UploadFile, 
    service: ImageToTextService = Depends(get_image_to_text_service)
):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["jpg", "jpeg", "png"]:
        raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a JPG or PNG image.")
    
    content = await file.read()
    size_mb = len(content) / (1024 * 1024)
    if size_mb > 10:
        raise HTTPException(status_code=400, detail="File size exceeds 10 MB limit.")
    
    image = Image(filename=file.filename, content=content)
    try:
        text = await service.convert(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"text": text}

