import asyncio
import websockets
import sys
from pydub import AudioSegment
import io

async def send_audio_data(ws_url, reference_audio_path, test_audio_path):
    async with websockets.connect(ws_url) as websocket:
        # Load reference audio
        reference_audio = AudioSegment.from_file(reference_audio_path, format="wav")
        reference_buffer = io.BytesIO()
        reference_audio.export(reference_buffer, format="wav")
        await websocket.send(reference_buffer.getvalue())
        print("Input Mantra sent.....")

        # Load test audio
        test_audio = AudioSegment.from_file(test_audio_path, format="wav")
        test_buffer = io.BytesIO()
        test_audio.export(test_buffer, format="wav")
        await websocket.send(test_buffer.getvalue())
        print("Streaming Chant now........")

        # Receive and print the comparison result
        comparison_result = await websocket.recv()
        print("Received:", comparison_result)

def main():
    ws_url = r"ws://localhost:8000/ws/audio"
    reference_audio_path = r"data\input.wav"  # Update this path
    test_audio_path = r"data\chant2.wav"  # Update this path

    asyncio.run(send_audio_data(ws_url, reference_audio_path, test_audio_path))

if __name__ == "__main__":
    main()
