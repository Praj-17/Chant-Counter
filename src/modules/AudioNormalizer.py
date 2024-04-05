import noisereduce as nr
import numpy as np
import librosa
# load data





class AudioNormalizer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def reduce_noise(data, rate):
        # Noise reduction
        reduced_noise = nr.reduce_noise(y=data, sr=rate)
        return reduced_noise

    @staticmethod
    def normalize_volume(data, rate):
        # Calculate the desired volume adjustment
        rms = np.sqrt(np.mean(data**2))
        desired_rms = 0.1
        gain = desired_rms / (rms + 1e-10)  # Avoid division by zero
        normalized_data = data * gain
        return normalized_data

    def process_audio(self, wav_file):
        # Load the audio file
        data, rate = librosa.load(wav_file, sr=None, mono=True, dtype=np.float32)
        # Reduce noise
        data_noised_reduced = self.reduce_noise(data, rate)
        # Normalize volume
        processed_data = self.normalize_volume(data_noised_reduced, rate)
        return processed_data, rate

