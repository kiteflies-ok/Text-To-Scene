from fastapi import APIRouter, UploadFile, BackgroundTasks
from ai_processing import summarizer, tts_generator
from animation_generator import manim_engine, blender_integration
from models.schemas import AnimationRequest, AnimationResponse
import uuid
import os

router = APIRouter()

@router.post("/process-text", response_model=AnimationResponse)
async def process_text(request: AnimationRequest):
    summary = summarizer.generate_summary(request.text)
    voiceover = tts_generator.generate_voiceover(summary["raw"])
    
    if request.animation_type == "2D":
        animation = manim_engine.generate_manim_animation(summary["scenes"])
    else:
        animation = blender_integration.generate_blender_animation(summary["scenes"])
    
    return {
        "animation": animation,
        "voiceover": voiceover,
        "summary": summary["raw"]
    }

@router.post("/upload-document")
async def upload_document(file: UploadFile):
    file_id = str(uuid.uuid4())
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, f"{file_id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"task_id": file_id}