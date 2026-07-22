import json


class KnowledgeAgent:

    def __init__(self):

        with open("data/faq.json", "r") as file:
            self.faq = json.load(file)

    def search(self, query):

        query = query.lower()

        for item in self.faq:

            question = item["question"].lower()

            if query in question or question in query:
                return item["answer"]

        return "No FAQ found."