from utils.gemini_client import GeminiClient
from prompts.planner_prompt import PLANNER_PROMPT


class PlannerAgent:

    def classify(self, coordinator_output):

        return coordinator_output["category"]