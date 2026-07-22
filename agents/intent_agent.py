from utils.gemini_client import GeminiClient
from prompts.intent_prompt import INTENT_PROMPT
import json


class IntentAgent:

    def identify(self, coordinator_output):

        return {
            "intent": coordinator_output["intent"],
            "order_id": coordinator_output["order_id"]
        }