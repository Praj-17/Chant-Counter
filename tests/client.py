import asyncio
import websockets
import sounddevice as sd
import numpy as np

async def send_audio_on_silence(websocket_url):
    async def audio_callback(indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        print(f"Volume: {volume_norm}")
        if volume_norm < silence_threshold:
            print("Silence detected, sending audio...")
            await websocket.send(audio_data)
            audio_data.clear()  # Clear the buffer after sending
        else:
            audio_data.extend(indata.copy())  # Add the current chunk to the buffer

    async with websockets.connect(websocket_url) as websocket:
        samplerate = 44100  # Sample rate in Hz
        duration = 1  # Duration to record before checking for silence
        silence_threshold = 0.5  # Adjust based on your noise level
        audio_data = bytearray()

        with sd.InputStream(callback=audio_callback, dtype='int16', channels=1, samplerate=samplerate):
            await asyncio.Future()  # Run forever



if __name__ == "__main__":
    # WebSocket server URL
    websocket_url = "ws://127.0.0.1:8000/ws/audio"

    # Run the async function in the event loop
    asyncio.get_event_loop().run_until_complete(send_audio_on_silence(websocket_url))
