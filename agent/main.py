import requests
from tools.calculator import evaluate_math
from tools.web_search import search

def run_agent():
    context = requests.get("http://localhost:8000/context").json()
    task = requests.get("http://localhost:8000/task").json()

    print("Objective:", task["objective"])

    # Simulate LLM understanding and routing logic
    if "capital" in task["objective"]:
        part1 = search("capital of France")
        part2 = evaluate_math("3*7")
        print(f"Answer: {part1} + {part2}")
    else:
        print("No tools matched.")

if __name__ == "__main__":
    run_agent()
