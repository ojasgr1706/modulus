import requests
from tools.calculator import evaluate_math
from tools.web_search import search
import sys

def process_query(query: str) -> str:
    # Rule-based tool routing (LLM-based routing can be added later)
    if any(op in query for op in ["+", "-", "*", "/", "**"]):
        return evaluate_math(query)
    elif any(keyword in query.lower() for keyword in ["who", "what", "where", "capital", "define", "search"]):
        return search(query)
    else:
        return "Sorry, I couldn't decide which tool to use for this query."

def chat_loop():
    print("🤖 Agent ready. Type 'exit' to quit.")
    while True:
        user_input = input("\nYou > ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        # You can also fetch and print context or task info here
        try:
            response = process_query(user_input)
            print(f"Agent > {response}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    chat_loop()
