from fastapi import APIRouter, Depends, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from typing import Annotated

from app.domain.models.image import Image
from app.application.services.image_to_audio_service import ImageToAudioService
from app.dependencies.image_to_audio_provider import get_image_to_audio_service

router = APIRouter()

@router.post("/img2audio")
async def img2audio(
    file: UploadFile,
    service: Annotated[ImageToAudioService, Depends(get_image_to_audio_service)]
):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["png", "jpg", "jpeg"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PNG and JPEG are allowed.")
    content = await file.read()
    size_mb = len(content) / (1024 * 1024)
    if size_mb > 10:
        raise HTTPException(status_code=400, detail="File size exceeds 10MB limit.")

    image = Image(filename=file.filename, content=content)
    try:
        audio_bytes = await service.convert(image)
        audio_stream = BytesIO(audio_bytes)
        return StreamingResponse(
            audio_stream,
            media_type="audio/mpeg",
            headers={"Content-Disposition": "attachment; filename=speech.mp3"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
