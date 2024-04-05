from src import TrascribeSRT
from src import ChantCounter




if __name__ == "__main__":
    transcriber = TrascribeSRT()

    input_audio = "input.wav"
    chant_audio = "chant.wav"

    input_transcription = transcriber.process_audio_and_transcribe(input_audio)
    chant_transcriptin = transcriber.process_audio_and_transcribe(chant_audio)
    print(input_transcription)
    print(chant_transcriptin)

    counter = ChantCounter()
    count = counter.count_chants(input=input_transcription["text"], chant=chant_transcriptin["text"])
    print(count)