from agents.coordinator_agent import CoordinatorAgent
from agents.planner_agent import PlannerAgent
from agents.intent_agent import IntentAgent
from agents.knowledge_agent import KnowledgeAgent

coordinator = CoordinatorAgent()
planner = PlannerAgent()
intent = IntentAgent()
knowledge = KnowledgeAgent()

while True:

    query = input("\nCustomer : ")

    if query.lower() == "exit":
        break

    data = coordinator.analyze(query)

    print("\nCoordinator Output")
    print(data)

    category = planner.classify(data)

    print("\nPlanner :", category)

    details = intent.identify(data)

    print("\nIntent :", details)

    answer = knowledge.search(query)

    print("\nKnowledge Agent:")
    print(answer)