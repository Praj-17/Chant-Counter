from modules import TrascribeSRT
from modules import ChantCounter
from modules import AudioUnderstandingGemini



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


if __name__ == "__main__":

    input_audio = r"data\input.mp3"
    chant_audio = r"data\chant2.mp3"

    counter = CountChantsFromAudio()

    count = counter.count_chants_gemini(input_audio, chant_audio)
    print(count)
