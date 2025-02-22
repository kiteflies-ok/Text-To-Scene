from fastapi import FastAPI, UploadFile
from langchain.chains import summarize
from manim import Scene, Text
import subprocess
from TTS.api import TTS
from fastapi.middleware.cors import CORSMiddleware
from celery import Celery
import uuid
import os
from routes.api import router as api_router
from utils.security import rate_limit_middleware
from utils.file_cleaner import setup_file_cleaner

app = FastAPI()

@app.post("/process-text")
async def process_text(text: str, animation_type: str = "2D"):
    # Text Summarization
    summary = summarize_text(text)
    
    # Generates Animation
    if animation_type == "2D":
        animation_path = generate_manim_animation(summary)
    else:
        animation_path = generate_blender_animation(summary)
    
    # Generates Voiceover
    voiceover_path = generate_voiceover(summary)
    
    return {
        "animation": animation_path,
        "voiceover": voiceover_path,
        "summary": summary
    }

def summarize_text(text: str):
    from langchain import OpenAI, PromptTemplate, LLMChain
    llm = OpenAI(temperature=0.7)
    template = "Summarize this text for animation: {text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    chain = LLMChain(prompt=prompt, llm=llm)
    return chain.run(text)

def generate_manim_animation(text: str):
    class GeneratedScene(Scene):
        def construct(self):
            t = Text(text)
            self.play(Write(t))
            self.wait(3)
    
    module = "animation_generator.manim_engine"
    scene = "GeneratedScene"
    output = "media/videos/1080p60/GeneratedScene.mp4"
    subprocess.run(f"manim -ql {module} {scene}", shell=True)
    return output

def generate_voiceover(text: str):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)
    output_path = "media/voiceover.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Celery configuration for background tasks
celery = Celery(__name__, broker=os.getenv("REDIS_URL"))

@app.post("/upload-document")
async def upload_document(file: UploadFile):
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"file_id": file_id}

@celery.task
def process_file_task(file_id: str):
    # OCR implementation here (using Tesseract/PyPDF2)
    # Text processing pipeline
    pass

app.middleware("http")(rate_limit_middleware)

# Routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Start the file cleaner when the app starts
@app.on_event("startup")
async def startup_event():
    setup_file_cleaner(interval_hours=1)  # Clean every hour