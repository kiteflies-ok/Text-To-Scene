from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from TTS.api import TTS
import os

def create_tts_engine():
    model_manager = ModelManager()
    
    model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/glow-tts")
    voc_path, voc_config_path, _ = model_manager.download_model("vocoder_models/en/ljspeech/multiband-melgan")
    
    return Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        vocoder_checkpoint=voc_path,
        vocoder_config=voc_config_path
    )

def generate_voiceover(text: str, output_dir: str = "media/voiceovers") -> str:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"voiceover_{hash(text)}.wav")
    
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts")
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path