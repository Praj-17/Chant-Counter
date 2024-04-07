from openai import OpenAI
from dotenv import load_dotenv
from .file_organizer import FileOrganizer
import os

# Load environment variables from .env file
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY") )
import os
import json




class ChantCounter:
    def __init__(self) -> None:
        self.system_prompt = os.getenv("system_prompt_file_location")
        self.user_prompt = os.getenv("user_prompt_file_location")
        with open(self.system_prompt, "r") as f:
            self.system_prompt = f.read()
            f.close()


        with open(os.getenv("constrain_file_location"), 'r') as json_file:
            self.constrain = json.load(json_file)
        self.fo = FileOrganizer()
    def run_openai(self, user_prompt,functions = []):
        response = """{"count":0}"""
        completion = client.chat.completions.create(
        model = os.getenv("model_name"),
        temperature = float(os.getenv("temperature")),
        messages=[
            {"role": "user", "content":self.system_prompt,
            "role": "user", "content":user_prompt}],
            functions=functions
        )
        try:
            response = completion.choices[0].message.function_call.arguments
        except Exception as e:
            print("Exception in detecting")

        return json.loads(response)
    def count_chants(self, input, chant):
        with open(self.user_prompt, "r") as f:
            prompt = f.read()
            prompt = prompt.format(input = input.strip(), chant = chant.strip())
            f.close()
        return self.run_openai(user_prompt=prompt, functions = [self.constrain])



if __name__ == "__main__":
    gen = ChantCounter()
    video_input = "test2.mp4"
    response =  gen.generate_questions(video_input, n  = 5)
    print(response)