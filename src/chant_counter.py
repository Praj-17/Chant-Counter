from modules import TrascribeSRT
from modules import ChantCounter



class CountChantsFromAudio:
    def __init__(self) -> None:
        self.transcriber = TrascribeSRT()
        self.counter = ChantCounter()
    def count_chants_audio(self, input_audio, chant_audio):
        
        input_transcription = self.transcriber.transcribe(input_audio)
        chant_transcription = self.transcriber.transcribe(chant_audio)

        print(input_transcription)
        print("##############################################")
        print(chant_transcription)
        return  self.counter.count_chants(input=input_transcription["text"], chant=chant_transcription["text"])
if __name__ == "__main__":

    input_audio = r"data\input.wav"
    chant_audio = r"data\chant2.wav"

    counter = CountChantsFromAudio()

    count = counter.count_chants_audio(input_audio, chant_audio)
    print(count)
