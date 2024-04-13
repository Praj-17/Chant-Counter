import asyncio
import websockets
from pydub import AudioSegment
import io

async def send_audio_data(ws_url, reference_audio_path, test_audio_path):
    async with websockets.connect(ws_url) as websocket:
        # Load reference audio
        reference_audio = AudioSegment.from_file(reference_audio_path, format="wav")
        reference_duration = len(reference_audio)  # Duration in milliseconds
        reference_buffer = io.BytesIO()
        reference_audio.export(reference_buffer, format="wav")
        await websocket.send(reference_buffer.getvalue())
        print("Input Mantra sent.....")

        # Load test audio
        test_audio = AudioSegment.from_file(test_audio_path, format="wav")
        
        # Determine the number of chunks of reference_duration that can be made from test_audio
        chunk_duration = reference_duration  # Duration of each chunk in milliseconds
        number_of_chunks = len(test_audio) // chunk_duration
        total_count = 0

        # Interleaved send and receive for each chunk
        for i in range(number_of_chunks):
            start_ms = i * chunk_duration
            end_ms = start_ms + chunk_duration
            chunk = test_audio[start_ms:end_ms]
            test_buffer = io.BytesIO()
            chunk.export(test_buffer, format="wav")
            await websocket.send(test_buffer.getvalue())
            print(f"Streaming Chant chunk {i+1} now........")
            
            # Receive and print the comparison result for the current chunk
            comparison_result = await websocket.recv()
            total_count += int(comparison_result)
            print(f"Received for chunk {i+1}:", comparison_result)
            # Optionally, send the comparison result to the frontend here
            # E.g., frontend_update(comparison_result)

        print("Total comparison count:", total_count)

def main():
    ws_url = r"ws://localhost:8000/ws/audio"
    reference_audio_path = r"data\input.wav"  # Update this path
    test_audio_path = r"data\chant2.wav"  # Update this path

    asyncio.run(send_audio_data(ws_url, reference_audio_path, test_audio_path))

if __name__ == "__main__":
    main()
