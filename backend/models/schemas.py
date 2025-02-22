from pydantic import BaseModel

class AnimationRequest(BaseModel):
    text: str
    animation_type: str = "2D"

class AnimationResponse(BaseModel):
    animation: str
    voiceover: str
    summary: str