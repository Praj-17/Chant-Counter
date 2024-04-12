
import  whisper_timestamped as whisper
import os

from .AudioNormalizer import AudioNormalizer
import numpy as np
import whisper
from scipy.io.wavfile import write
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()





class TrascribeSRT():
  def __init__(self) -> None:
    model_size = os.getenv("model_size")
    self.model = whisper.load_model(model_size, device="cpu")
    self.audio_normalizer = AudioNormalizer()
  def transcribe(self, wav_file):
    #use the WhisperModel to transcribe the mp3 file
    audio = whisper.load_audio(wav_file)
    # results = self.model.transcribe(wav_file, beam_size=5)
    return whisper.transcribe(self.model, audio, language = "en")
  def process_audio_and_transcribe(self, audio_path):
        # Process the audio with the normalizer
        processed_data, rate = self.audio_normalizer.process_audio(audio_path)
        
        # Convert your processed data to the appropriate int16 format expected by Whisper
        processed_data_int16 = np.int16(processed_data * 32767)
        
        # Create a temporary file to save the processed audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            # Save the processed audio data to the temporary file
            write(tmp_file.name, rate, processed_data_int16)
            
            # Load the temporary file with Whisper for transcription
            result = self.transcribe(wav_file=tmp_file.name)
        
        # Clean up: Delete the temporary file
        os.remove(tmp_file.name)
        
        return result
    
  


if __name__ == "__main__":
    print("Transcribing the audio now....This may take a while on CPU")
    ts = TrascribeSRT()
    results = ts.transcribe('input.opus')
    print(results)