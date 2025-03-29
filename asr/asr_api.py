import io
import torch
import librosa
import soundfile as sf
from fastapi import FastAPI, File, UploadFile
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from pydantic import BaseModel
from typing import Dict
from transformers import AutoProcessor, AutoModelForCTC
import uvicorn

app = FastAPI()

processor = AutoProcessor.from_pretrained("facebook/wav2vec2-large-960h")
model = AutoModelForCTC.from_pretrained("facebook/wav2vec2-large-960h")

def transcribe_audio(audio_bytes: bytes):
    # Load audio file
    with io.BytesIO(audio_bytes) as audio_buffer:
        audio, sr = librosa.load(audio_buffer, sr=16000) # Load at 16kHz
    
    # Convert to tensor using processor
    input_values = processor(audio, return_tensors="pt", sampling_rate=16000).input_values
    
    # Perform inference
    with torch.no_grad():
        logits = model(input_values).logits
    
    # Get predicted transcription
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    
    # Get duration
    duration = len(audio) / sr
    
    # Return transcription and duration
    return transcription, f"{duration:.1f}"

@app.post("/asr", response_model=Dict[str, str])
async def asr_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    transcription, duration = transcribe_audio(audio_bytes)

    # Delete the file after processing
    await file.close()

    return {"transcription": transcription, "duration": duration}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)