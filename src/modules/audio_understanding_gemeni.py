import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class AudioUnderstandingGemini:
    def __init__(self) -> None:
        with open(os.getenv("gemini_prompt_file_location"), "r") as file:
            self.prompt = file.read()
        self.model = genai.GenerativeModel(os.getenv("gemini_model_name"))
    def extract_numbers(self, s):
        # Extracting all numeric characters from the string
        numbers = ''.join([char for char in s if char.isdigit()])
        # Converting the concatenated string to an integer
        numbers = numbers.strip()
        return int(numbers) if numbers else 0  # returns 0 if no digits found

    def count_chants(self, input_audio, chant_aduio):
        response = self.model.generate_content([self.prompt, input_audio, chant_aduio])
        return self.extract_numbers(response.text)

if __name__ == "__main__":
    input_file  = genai.upload_file(path=r'data\input.mp3', display_name= "input")
    chant  = genai.upload_file(path=r'data\chant.mp3', display_name= "chant")