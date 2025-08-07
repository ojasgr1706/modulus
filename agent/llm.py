import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_tool_choice(user_input, tools_dict):
    tools_description = "\n".join([f"- {k}: {v['description']}" for k, v in tools_dict.items()])

    prompt = f"""
You are a smart agent. Based on the user's question, decide if one of the following tools should be used.

Available tools:
{tools_description}

User question: "{user_input}"

If a tool should be used, respond in JSON like:
{{"tool": "tool_name", "input": "input for the tool"}}

If no tool is needed, respond:
{{"tool": null, "input": null}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
