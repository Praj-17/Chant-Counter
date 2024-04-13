from src.modules import TrascribeSRT
from src.modules import ChantCounter
from src.modules import AudioUnderstandingGemini
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class CountChantsFromAudio:
    def __init__(self) -> None:
        self.transcriber = TrascribeSRT()
        self.counter = ChantCounter()
        self.gemini = AudioUnderstandingGemini()
    def count_chants_audio(self, input_audio, chant_audio):
        
        input_transcription = self.transcriber.transcribe(input_audio)
        chant_transcription = self.transcriber.transcribe(chant_audio)
        return  self.counter.count_chants(input=input_transcription["text"], chant=chant_transcription["text"])
    def count_chants_gemini(self, input_audio, chant_audio):
        return self.gemini.count_chants(input_audio, chant_audio)

class CountChantsFromAudioGemini:
    def __init__(self, input_audio) -> None:
        self.input_audio  = genai.upload_file(path=input_audio, display_name= "input")
        self.gemini = AudioUnderstandingGemini()
    def count_chants_gemini(self,chant_audio):
        chant  = genai.upload_file(path=chant_audio, display_name= "chant")
        return self.gemini.count_chants(self.input_audio, chant)


if __name__ == "__main__":

    input_audio = r"data\input.mp3"
    chant_audio = r"data\chant2.mp3"

    counter = CountChantsFromAudio()

    count = counter.count_chants_gemini(input_audio, chant_audio)
    print(count)
