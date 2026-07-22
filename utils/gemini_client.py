from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


class GeminiClient:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.model = "gemini-3.5-flash-lite"

    def generate(self, prompt: str):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text.strip()