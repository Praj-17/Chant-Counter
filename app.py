from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import tempfile
import shutil
from pydub import AudioSegment
import numpy as np
from src.chant_counter import CountChantsFromAudioGemini
import io
import os

app = FastAPI()

@app.websocket("/ws/audio")
async def audio_processor(websocket: WebSocket):
    await websocket.accept()
    reference_audio_path = None  # To store reference audio file path   
  
    try:
        # First message should be the reference audio
        reference_audio_data = await websocket.receive_bytes()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
            tmp.write(reference_audio_data)
            reference_audio_path = tmp.name
        chant_counter = CountChantsFromAudioGemini(reference_audio_path)
 

        while True:
            # Continuously receive audio data from the client
            audio_data = await websocket.receive_bytes()
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
                tmp.write(audio_data)
                audio_path = tmp.name

            # Count the chants in the received audio compared to the reference audio
            chant_count = chant_counter.count_chants_gemini(audio_path)

            # Send the chant count result back to the client
            await websocket.send_text((str(chant_count)))

            # Cleanup the temporary file
            os.remove(audio_path)

    except WebSocketDisconnect:
        print("Client disconnected")
        if reference_audio_path:
            os.remove(reference_audio_path)

# Optional: Endpoint to check server status
@app.get("/")
def read_root():
    return {"message": "Server is running"}
