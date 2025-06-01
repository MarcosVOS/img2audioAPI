from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from typing import Annotated
from io import BytesIO
from app.application.services.text_to_audio_service import TextToAudioService
from app.domain.infrastructure.openai_tts import OpenAIAudioConverter
from app.dependencies.text_to_audio_provider import get_text_to_audio_service
import config

router = APIRouter()
@router.get("/text2audio")
async def text2audio(
    text: Annotated[str, Query(min_length=1, max_length=5000)],
    service: Annotated[TextToAudioService, Depends(get_text_to_audio_service)]
):
    try:
        audio_bytes = await service.convert(text)
        audio_stream = BytesIO(audio_bytes)
        return StreamingResponse(
            audio_stream,
            media_type="audio/mpeg",
            headers={"Content-Disposition": "attachment; filename=speech.mp3"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))