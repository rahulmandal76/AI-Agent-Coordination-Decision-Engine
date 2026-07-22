import json

from utils.gemini_client import GeminiClient
from prompts.coordinator_prompt import COORDINATOR_PROMPT


class CoordinatorAgent:

    def __init__(self):
        self.gemini = GeminiClient()

    def analyze(self, query):

        prompt = COORDINATOR_PROMPT.format(query=query)

        response = self.gemini.generate(prompt)

        # Remove markdown if Gemini returns ```json ... ```
        response = response.replace("```json", "")
        response = response.replace("```", "").strip()

        try:
            return json.loads(response)

        except Exception as e:
            print("JSON Parsing Error:", e)
            print(response)

            return {
                "category": "GENERAL",
                "intent": "GENERAL_QUERY",
                "order_id": None,
                "tool": "NONE",
                "needs_tool": False
            }