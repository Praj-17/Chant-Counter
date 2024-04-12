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
    def extract_only_number(self, response):
        # This regular expression finds one or more digits
        matches = re.findall(r'\d+', response)
        if matches:
            return int(matches[0])  # Convert the first match to an integer and return it
        else:
            return "No number found"

    def count_chants(self, input_audio, chant_aduio):
        input_file  = genai.upload_file(path=input_audio, display_name= "input")
        chant  = genai.upload_file(path=chant_aduio, display_name= "chant")
        response = str(self.model.generate_content([self.prompt, input_file, chant]))
        return self.extract_only_number(response)

if __name__ == "__main__":
    input_file  = genai.upload_file(path=r'data\input.mp3', display_name= "input")
    chant  = genai.upload_file(path=r'data\chant.mp3', display_name= "chant")