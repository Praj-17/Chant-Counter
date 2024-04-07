from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

async def process_audio_chunk(audio_chunk):
    """
    Async function to process audio data.
    Replace this with your actual audio processing logic.
    """
    # Simulate asynchronous processing of audio chunk
    await asyncio.sleep(0.1)  # Simulating processing delay
    return f"Processed {len(audio_chunk)} bytes"

@app.websocket("/ws/audio")
async def websocket_audio_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for streaming audio data.
    Clients connect and send audio data which is processed and responded back.
    """
    await websocket.accept()
    try:
        while True:
            audio_data = await websocket.receive_bytes()
            if audio_data:
                # Process the received audio chunk
                processed_data = await process_audio_chunk(audio_data)
                # Send back the processed data
                await websocket.send_text(processed_data)
            else:
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()

@app.get("/")
async def root():
    """
    Simple endpoint to verify that the server is running.
    """
    return {"message": "WebSocket audio processing server is running"}
